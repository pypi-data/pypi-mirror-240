"""Defines a launcher for Slurm jobs.

Steps
-----

1. Stages the environment to a new working directory
2. Writes an ``sbatch.sh`` file
3. Schedules ``sbatch.sh`` file

This allows for repeatability by just scheduling the same `sbatch.sh` file.
"""

import logging
import os
import re
import signal
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import cast

from omegaconf import II, MISSING, DictConfig, OmegaConf

from ml.core.config import conf_field
from ml.core.env import get_slurm_conf_path, get_stage_dir
from ml.core.registry import Objects, project_dirs, register_launcher, register_trainer
from ml.launchers.base import BaseLauncher, BaseLauncherConfig
from ml.scripts.train import train_main
from ml.trainers.base import BaseTrainer
from ml.utils.distributed import (
    get_random_port,
    is_master,
    set_init_method,
    set_master_addr,
    set_master_port,
    set_rank,
    set_world_size,
)
from ml.utils.logging import configure_logging
from ml.utils.staging import stage_environment
from ml.utils.torch_distributed import init_parallelism, init_process_group_from_backend

logger = logging.getLogger(__name__)

OmegaConf.register_new_resolver("ml.get_random_slurm_port", get_random_port, replace=True)

SBATCH_TEMPLATE: str = """
#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --partition={partition}
#SBATCH --requeue
#SBATCH --signal=USR1@60
#SBATCH --time={time_limit}
#SBATCH --comment='{comment}'
#SBATCH --nodes={num_nodes}
#SBATCH --ntasks-per-node={tasks_per_node}
#SBATCH --cpus-per-task={cpus_per_task}
#SBATCH --gres={gres}
#SBATCH --gpu-bind={gpu_bind}
#SBATCH --output={output_path}
#SBATCH --error={error_path}
#SBATCH --open-mode=append
#SBATCH --chdir={stage_dir}
{extra_sbatch_lines}

# Sets the environment variables.
export SLURM_EXPORT_ENV=ALL
export STAGE_DIR={stage_dir}
export PYTHONPATH={pythonpath}
export MASTER_PORT={master_port}

# Set some debugging flags.
export TORCH_DISTRIBUTED_DEBUG=DETAIL
export TORCH_SHOW_CPP_STACKTRACES=1
export NCCL_DEBUG=1
export SHOW_FULL_IMPORT_ERROR=1
export IGNORE_REGISTRY_CACHE=1

# Make a new line in the stdout file.
echo ""
echo "***"
echo "Job ID: ${{SLURM_JOBID}} - $(date)"
echo "***"
echo ""

# Also make a new line in the stderr file.
echo "" >&2
echo "***" >&2
echo "Job ID: ${{SLURM_JOBID}} - $(date)" >&2
echo "***" >&2
echo "" >&2

# Runs the training command.
srun \\
    --nodes={num_nodes} \\
    --ntasks-per-node={tasks_per_node} \\
    --cpus-per-task={cpus_per_task} \\
    --gres={gres} \\
    --gpu-bind={gpu_bind} \\
    python -m ml.launchers.slurm {config_path}

echo ""
""".strip()

DEFAULT_MASTER_PORT_STR = "29500"


@dataclass
class SlurmConfItem:
    key: str = conf_field(MISSING)
    partition: str = conf_field(MISSING)
    gpus_per_node: int = conf_field(MISSING)
    cpus_per_gpu: int = conf_field(MISSING)
    num_nodes: int = conf_field(MISSING)
    gpu_type: str | None = conf_field(None)
    exclusive: bool = conf_field(False)


@dataclass
class SlurmConf:
    configurations: list[SlurmConfItem] = conf_field([], help="Slurm configuration options")

    @classmethod
    def load(cls) -> "SlurmConf":
        conf_path = get_slurm_conf_path()
        if not conf_path.exists():
            raise FileNotFoundError(
                f"Slurm configuration file not found: {conf_path} "
                "Update ML_SLURM_CONF environment variable to point to the correct configuration path"
            )
        conf = OmegaConf.load(conf_path)
        if not OmegaConf.is_dict(conf):
            raise ValueError(f"Expected a dict config, got: {conf}")
        return OmegaConf.merge(OmegaConf.structured(cls), conf)  # type: ignore[return-value]

    def save(self) -> None:
        conf_path = get_slurm_conf_path()
        OmegaConf.save(self, conf_path)


def set_slurm_rank_and_world_size() -> tuple[int, int]:
    node_id = int(os.environ["SLURM_NODEID"])
    local_id = int(os.environ["SLURM_LOCALID"])
    tasks_per_node = int(os.environ["SLURM_NTASKS_PER_NODE"])
    num_nodes = int(os.environ["SLURM_NNODES"])
    rank = node_id * tasks_per_node + local_id
    world_size = num_nodes * tasks_per_node
    set_rank(rank)
    set_world_size(world_size)
    return rank, world_size


def set_slurm_master_addr_and_port() -> str:
    node_list = os.environ.get("SLURM_STEP_NODELIST")
    if node_list is None:
        node_list = os.environ.get("SLURM_JOB_NODELIST")
    assert node_list is not None, "`SLURM_JOB_NODELIST` environment variable not set"
    hostnames = subprocess.check_output(["scontrol", "show", "hostnames", node_list])
    host = hostnames.split()[0].decode("utf-8")
    port = int(os.environ.get("MASTER_PORT", DEFAULT_MASTER_PORT_STR))
    set_master_addr(host)
    set_master_port(port)
    return host


def requeue_job() -> None:
    if is_master():
        if "SLURM_JOB_ID" in os.environ:
            cmd = ["scontrol", "requeue", os.environ["SLURM_JOB_ID"]]
            logger.info("Running %s", " ".join(cmd))
            subprocess.check_call(cmd)
        else:
            logger.info("SLURM_JOB_ID environment variable not found; not requeueing")


@dataclass
class SlurmLauncherConfig(BaseLauncherConfig):
    conf_key: str = conf_field(II("oc.env:SLURM_DEFAULT_KEY,missing"), help="Slurm config key to use")
    time_limit: str = conf_field(II("oc.env:SLURM_TIME_LIMIT,3-00:00:00"), help="Time limit string")
    num_jobs: int = conf_field(1, help="Number of redundant jobs to launch")
    comment: str | None = conf_field(None, help="An optional comment to add to the experiment")
    master_port: int = conf_field(II("ml.get_random_slurm_port:1337"), help="The master port to use")
    model_parallelism: int = conf_field(1, help="The number of model parallel processes")
    pipeline_parallelism: int = conf_field(1, help="The number of pipeline parallel processes")
    backend: str | None = conf_field(None, help="The distributed backend")
    model_parallel_backend: str | None = conf_field(None, help="The model parallel backend")
    pipeline_parallel_backend: str | None = conf_field(None, help="The pipeline parallel backend")
    data_parallel_backend: str | None = conf_field(None, help="The data parallel backend")
    account: str | None = conf_field(None, help="The account to use, if required")


@register_launcher("slurm", SlurmLauncherConfig)
class SlurmLauncher(BaseLauncher[SlurmLauncherConfig]):
    def _write_sbatch_file(self, trainer: BaseTrainer) -> Path:
        # Loads the slurm configuration file.
        slurm_confs = SlurmConf.load()
        if self.config.conf_key == "missing":
            if len(slurm_confs.configurations) == 0:
                raise KeyError(f"No Slurm configurations found in the configuration file {get_slurm_conf_path()}")
            slurm_conf = slurm_confs.configurations[0]
        else:
            for slurm_conf in slurm_confs.configurations:
                if slurm_conf.key == self.config.conf_key:
                    break
            else:
                slurm_confs_str = OmegaConf.to_yaml(slurm_confs)
                raise KeyError(f"Slurm config key not found: {self.config.conf_key}. Options:\n\n{slurm_confs_str}")

        # Gets some configuration options.
        gpus_per_node = slurm_conf.gpus_per_node
        gpu_type = slurm_conf.gpu_type
        tasks_per_node = gpus_per_node
        cpus_per_task = slurm_conf.cpus_per_gpu
        exclusive = slurm_conf.exclusive

        # GRES and GPU Bind SBatch options.
        gres = f"gpu:{gpus_per_node}" if gpu_type is None else f"gpu:{gpu_type}:{gpus_per_node}"
        gpu_bind = f"map_gpu:{','.join(str(i) for i in range(gpus_per_node))}"

        # Gets extra SBatch options.
        sbatch_lines: list[str] = []
        if "EMAIL" in os.environ:
            sbatch_lines += [f"--mail-user={os.environ['EMAIL']}", "--mail-type=ALL"]
        if self.config.account is not None:
            sbatch_lines += [f"--account={self.config.account}"]
        if exclusive:
            sbatch_lines += ["--exclusive"]

        # Writes all Slurm stuff (including logs) to this folder.
        log_dir = trainer.exp_dir / "logs"
        log_dir.mkdir(exist_ok=True, parents=True)
        sbatch_path = trainer.exp_dir / "sbatch.sh"

        # Stages all files to a new directory.
        stage_dir = stage_environment(project_dirs.paths[1:], get_stage_dir())

        # Gets the python path with the new output directory.
        python_path_parts = [str(stage_dir)] + os.environ.get("PYTHONPATH", "").split(":")
        python_path = ":".join(p for p in python_path_parts if p)

        # Comment miscellaneous stuff here.
        comments: list[str] = []
        if self.config.comment is not None:
            comments += [self.config.comment]
        comments += [f"Log directory: {trainer.exp_dir}"]
        comments += [f"Code location: {stage_dir}"]

        # Saves the config that is used to launch the Slurm job.
        trainer.save_config()

        # Builds the SBatch file.
        sbatch_file = SBATCH_TEMPLATE.format(
            job_name=trainer.exp_name,
            partition=slurm_conf.partition,
            time_limit=self.config.time_limit,
            comment="; ".join(comments),
            num_nodes=slurm_conf.num_nodes,
            tasks_per_node=tasks_per_node,
            cpus_per_task=cpus_per_task,
            gres=gres,
            gpu_bind=gpu_bind,
            output_path=log_dir / "slurm_out.txt",
            error_path=log_dir / "slurm_err.txt",
            extra_sbatch_lines="\n".join(f"#SBATCH {line}" for line in sbatch_lines),
            stage_dir=stage_dir,
            pythonpath=python_path,
            master_port=self.config.master_port,
            config_path=trainer.exp_dir / "config.yaml",
            lock_file_path=trainer.exp_dir / ".lock_running",
        )

        with open(sbatch_path, "w", encoding="utf-8") as f:
            f.write(sbatch_file)
        logger.info("Wrote sbatch file to %s", sbatch_path)

        return sbatch_path

    def launch(self) -> None:
        trainer = register_trainer.build_entry_non_null(self.raw_config)

        sbatch_path = self._write_sbatch_file(trainer)

        # Call `sbatch` on the given file.
        all_run_ids: list[str] = []
        for _ in range(self.config.num_jobs):
            command = ["sbatch", str(sbatch_path)]
            if all_run_ids:
                command += ["--dependency", all_run_ids[-1]]
            proc = subprocess.Popen(  # pylint: disable=consider-using-with
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            assert proc is not None and proc.stdout is not None
            proc.wait()
            log_line = proc.stdout.read().decode("utf-8").strip()
            run_ids = re.findall(r"Submitted batch job (\d+)", log_line)
            assert len(run_ids) == 1, f"Unexpected log line: {log_line}"
            all_run_ids += [run_ids[0]]

        run_ids_str = "".join(f"\n - {run_id}" for run_id in all_run_ids)
        logger.info("Launched %d job(s):%s", len(all_run_ids), run_ids_str)

        trainer.add_lock_file("scheduled", exists_ok=False)


def slurm_main() -> None:
    args = sys.argv[1:]
    assert len(args) == 1, f"Unexpected arguments to `slurm_main`: {sys.argv}"

    # Adds the stage directories as project directories.
    for sub_dir in get_stage_dir(allow_default=False).iterdir():
        if sub_dir.is_dir():
            project_dirs.add(sub_dir)

    # Loads the raw config.
    raw_config = cast(DictConfig, OmegaConf.load(args[0]))
    if not OmegaConf.is_dict(raw_config):
        raise ValueError(f"Expected a dict config, got: {raw_config}")

    # Gets the launcher config from the raw config.
    assert (launcher := register_launcher.build_entry(raw_config)) is not None
    assert isinstance(launcher, SlurmLauncher), f"Expected a SlurmLauncher, got: {launcher}"
    cfg = launcher.config

    # Sets environment variables from Slurm environment variables.
    set_slurm_master_addr_and_port()
    rank, world_size = set_slurm_rank_and_world_size()

    # Sets the initialization method and configures per-rank logging.
    set_init_method("env://")
    configure_logging(rank=rank, world_size=world_size)
    init_process_group_from_backend()

    # Sets model parallelism.
    init_parallelism(
        model_parallelism=cfg.model_parallelism,
        pipeline_parallelism=cfg.pipeline_parallelism,
        mp_backend=cfg.backend if cfg.model_parallel_backend is None else cfg.model_parallel_backend,
        pp_backend=cfg.backend if cfg.pipeline_parallel_backend is None else cfg.pipeline_parallel_backend,
        dp_backend=cfg.backend if cfg.data_parallel_backend is None else cfg.data_parallel_backend,
    )

    assert (trainer := register_trainer.build_entry(raw_config)) is not None
    trainer.add_lock_file("running", exists_ok=True)
    trainer.remove_lock_file("scheduled", missing_ok=True)

    # Detect timeout and requeue the job.
    trainer.add_signal_handler(signal.SIGUSR1, requeue_job)

    objs = Objects(raw_config, trainer=trainer)
    train_main(raw_config, objs)


if __name__ == "__main__":
    # python -m lm.launchers.slurm
    slurm_main()
