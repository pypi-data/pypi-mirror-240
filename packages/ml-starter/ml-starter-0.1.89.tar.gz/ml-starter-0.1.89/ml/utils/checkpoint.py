"""Defines checkpoint utility functions.

These functions can be used to load a model from an arbitrary config file
and checkpoint. Note that there might be some issues if you move the checkpoint
around places.
"""

import logging
import re
import tempfile
from pathlib import Path
from typing import Any, TypeVar, cast

import torch
import yaml
from omegaconf import MISSING, Container, DictConfig, OmegaConf
from omegaconf._utils import get_yaml_loader
from torchvision.datasets.utils import download_url

from ml.core.env import get_model_dir, set_ml_config_path
from ml.core.registry import Objects, register_model, register_task
from ml.models.base import BaseModel
from ml.tasks.base import BaseTask
from ml.trainers.base import BaseTrainer
from ml.utils.data import check_md5, check_sha256
from ml.utils.device.auto import detect_device
from ml.utils.timer import Timer

logger = logging.getLogger(__name__)

T = TypeVar("T")


def is_missing(cfg: Any, key: str) -> bool:  # noqa: ANN401
    """Utility function for checking if a config key is missing.

    This is for cases when you are using a raw dataclass rather than an
    OmegaConf container but want to treat them the same way.

    Args:
        cfg: The config to check
        key: The key to check

    Returns:
        Whether or not the key is missing a value in the config
    """
    if isinstance(cfg, Container) and OmegaConf.is_missing(cfg, key):
        return True
    if getattr(cfg, key) is MISSING:
        return True
    return False


def instantiate_config(config: str | Path | DictConfig | dict) -> Objects:
    """Builds the objects from the raw config.

    Args:
        config: The config to use. If a string or a Path, it is expected to
            be a path to a YAML file.

    Returns:
        The instantiated objects.
    """
    if isinstance(config, (str, Path)):
        set_ml_config_path(Path(config))
        config = cast(DictConfig, OmegaConf.load(config))
        if not OmegaConf.is_dict(config):
            raise ValueError(f"Expected config to be a dict, got {type(config)}")
    elif isinstance(config, dict):
        config = OmegaConf.create(config)
    Objects.update_config(config)
    Objects.resolve_config(config)
    return Objects.parse_raw_config(config)


def get_checkpoint_path(trainer: BaseTrainer, config_path: str | Path, ckpt_path: str | Path | None) -> Path:
    if ckpt_path is not None:
        ckpt_path = Path(ckpt_path)
        if ckpt_path.exists():
            return ckpt_path
        logger.warning("Could not find the passed checkpoint at %s", ckpt_path)

    # Tries loading the checkpoint that the trainer thinks exists.
    ckpt_path = trainer.get_ckpt_path()
    if ckpt_path.exists():
        return ckpt_path
    logger.warning("Could not find trainer checkpoint at %s", ckpt_path)

    # Tries loading other checkpoints.
    config_path = Path(config_path)
    ckpt_path = config_path.parent / "ckpt.pt"
    if ckpt_path.exists():
        return ckpt_path
    logger.warning("Could not find checkpoint at %s", ckpt_path)

    # Searches for a checkpoint in the same directory as the config.
    ckpt_paths = list(config_path.parent.rglob("ckpt*.pt"))
    if ckpt_paths:
        return max(ckpt_paths, key=lambda p: p.stat().st_mtime)
    logger.warning("Could not find checkpoints in config directory %s", config_path.parent)

    raise RuntimeError("Could not find a checkpoint to load")


def load_model_and_task(
    config_path: str | Path | None = None,
    ckpt_path: str | Path | None = None,
    to_device: bool = True,
    missing_ckpt_okay: bool = False,
) -> tuple[BaseModel, BaseTask]:
    """Loads a trained checkpoint from a config, and optional checkpoint path.

    Args:
        config_path: The path to the config file.
        ckpt_path: The path to the checkpoint file; if None, the latest
            checkpoint will be used. This defaults to first checking in an
            adjacent ``checkpoints`` directory for a ``ckpt.pt`` file, or else
            checking for the checkpoint file in the same directory as the
            config.
        to_device: Whether to move the model to the device specified in the
            config.
        missing_ckpt_okay: Whether to return a model and task even if the
            checkpoint is missing.

    Returns:
        The model and task loaded from the checkpoint

    Raises:
        ValueError: If both ``config_path`` and ``ckpt_path`` are None.
        RuntimeError: If the checkpoint is missing and `missing_ckpt_okay` is
            False.
    """
    with Timer("loading checkpoint"):
        concrete_ckpt_path: str | Path | None = None

        trainer: BaseTrainer

        if config_path is None:
            if ckpt_path is None:
                raise ValueError("Must provide either a config path or a checkpoint path")

            ckpt = torch.load(ckpt_path, map_location="cpu")
            if "config" not in ckpt:
                raise ValueError("Could not find a config in the checkpoint")
            concrete_ckpt_path = ckpt_path
            set_ml_config_path(Path(ckpt_path).parent / "config.yaml")
            config_yaml = yaml.load(ckpt["config"], Loader=get_yaml_loader())
            config = OmegaConf.create(config_yaml)

            trainer = BaseTrainer(config.trainer)

        else:
            set_ml_config_path(Path(config_path))
            config = cast(DictConfig, OmegaConf.load(config_path))
            trainer = BaseTrainer(config.trainer)

            # Uses the dummy trainer to load the checkpoint.
            try:
                concrete_ckpt_path = get_checkpoint_path(trainer, config_path, ckpt_path)
            except RuntimeError:
                if missing_ckpt_okay:
                    logger.exception("Could not load checkpoint")
                else:
                    raise

        model = register_model.build_entry_non_null(config)
        task = register_task.build_entry_non_null(config)
        if concrete_ckpt_path is not None:
            trainer.load_checkpoint(concrete_ckpt_path, task, model)

        if to_device:
            device = detect_device()
            device.module_to(model, with_dtype=False)
            device.module_to(task, with_dtype=False)

    return model, task


def ensure_downloaded(
    url: str,
    *dnames: str,
    md5: str | None = None,
    sha256: str | None = None,
    is_tmp: bool = False,
    recheck_hash: bool = False,
) -> Path:
    """Ensures that a checkpoint URL has been downloaded.

    This basically just provides a nice way of organizing pre-trained models,
    by saving them to a consistent location.

    Args:
        url: The URL to download.
        dnames: The directory to download to (note that this is relative to the
            model directory). The final name should be the file name
        md5: The MD5 hash of the file, if known.
        sha256: The SHA256 hash of the file, if known.
        is_tmp: If set, use ``tmp/`` instead of ``get_model_dir()``
        recheck_hash: Whether to recheck the hash of the file if it already
            exists.

    Returns:
        The path to the downloaded file.
    """
    assert len(dnames) >= 1, "Must provide at least 1 directory name"
    filepath = Path(tempfile.mkdtemp("models")) if is_tmp else get_model_dir()
    for dname in dnames:
        filepath = filepath / dname
    (root := filepath.parent).mkdir(parents=True, exist_ok=True)

    def check_hashes() -> bool:
        return filepath.is_file() and check_sha256(filepath, sha256) and check_md5(filepath, md5)

    def download_file() -> None:
        download_url(url, root=root, filename=filepath.name)
        assert filepath.is_file(), f"Failed to download {url} to {filepath}"
        if not check_hashes():
            filepath.unlink()
            raise RuntimeError(f"Hashes for {url} do not match")

    # If the file does not exist, download it and check the hashes.
    if not filepath.exists():
        download_file()

    # By default, assume the downloaded file hash is correct.
    if not recheck_hash:
        return filepath

    # Check the file hashes again, to ensure the file was not corrupted.
    if not check_hashes():
        filepath.unlink()
        download_file()

    return filepath


def get_state_dict_prefix(
    ckpt: dict[str, T],
    prefix: str | None = None,
    suffix: str | None = None,
    regexp: re.Pattern[str] | None = None,
) -> dict[str, T]:
    """Returns the parts of a checkpoint which begin with a prefix.

    Args:
        ckpt: The checkpoint to modify
        prefix: The prefix to clip
        suffix: The suffix to clip
        regexp: The regexp to search for (doesn't modify any keys)

    Returns:
        The modified checkpoint
    """
    if prefix is not None:
        ckpt = {k[len(prefix) :]: v for k, v in ckpt.items() if k.startswith(prefix)}
    if suffix is not None:
        ckpt = {k[: -len(suffix)]: v for k, v in ckpt.items() if k.endswith(suffix)}
    if regexp is not None:
        ckpt = {k: v for k, v in ckpt.items() if regexp.match(k)}
    return ckpt
