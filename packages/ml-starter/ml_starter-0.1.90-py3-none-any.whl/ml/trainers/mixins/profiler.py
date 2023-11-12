"""Defines a trainer mixin for profiling PyTorch models.

This can be enabled by setting ``trainer.profiler.enabled=true`` in your
configuration file. It will run the first few steps of training with the
profiler enabled, and then log a report of the results to the log directory.
"""

import contextlib
import datetime
import logging
import time
from dataclasses import dataclass
from typing import Any, ContextManager, Iterator, TypeVar

import torch

from ml.core.config import conf_field
from ml.core.state import State
from ml.trainers.base import BaseTrainer, BaseTrainerConfig, ModelT, TaskT
from ml.trainers.mixins.step_wrapper import StepContextMixin, StepType

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class Profiler:
    enabled: bool = conf_field(False, help="If profiling should be enabled")
    record_shapes: bool = conf_field(False, help="If set, record tensor shapes")
    profile_memory: bool = conf_field(False, help="If set, profile PyTorch memory")
    with_stack: bool = conf_field(False, help="Record source information (file and line number) for ops")
    with_flops: bool = conf_field(False, help="Use formula to estimate the FLOPs of specific operations")
    with_modules: bool = conf_field(False, help="Record module hierarchy (including function names)")
    wait_steps: int = conf_field(10, help="Number of initial waiting steps")
    warmup_steps: int = conf_field(10, help="Number of profiler warmup steps")
    active_steps: int = conf_field(10, help="Number of profiler active steps")
    repeat_steps: int = conf_field(1, help="Number of profiler repetitions")
    skip_first_steps: int = conf_field(10, help="Number of profiler steps to skip at first")
    table_size: int = conf_field(10, help="Number of profiling ops to print")


STEPS_TO_TIME: set[StepType] = {
    "backward",
    "clip_grads",
    "forward",
    "get_single_loss",
    "log_losses",
    "on_step_end",
    "on_step_start",
    "step",
    "write_logs",
    "zero_grads",
}


@dataclass
class ProfilerTrainerConfig(BaseTrainerConfig):
    profiler: Profiler = conf_field(Profiler(), help="Profiler configuration")


ProfilerTrainerConfigT = TypeVar("ProfilerTrainerConfigT", bound=ProfilerTrainerConfig)


class ProfilerTrainerMixin(
    StepContextMixin[ProfilerTrainerConfigT, ModelT, TaskT],
    BaseTrainer[ProfilerTrainerConfigT, ModelT, TaskT],
):
    """Defines a trainer mixin for enabling the PyTorch profiler."""

    def __init__(self, config: ProfilerTrainerConfigT) -> None:
        super().__init__(config)

        self.step_times: dict[StepType, float] = {}

    def step_context(self, step: StepType) -> ContextManager:
        ctx = super().step_context(step)

        if step not in STEPS_TO_TIME:
            return ctx

        @contextlib.contextmanager
        def wrapped_ctx() -> Iterator[Any]:
            start_time = time.time()

            if self.config.profiler.enabled:
                with ctx as a, torch.profiler.record_function(step) as b:
                    yield a, b
            else:
                with ctx as a:
                    yield a

            step_time = time.time() - start_time
            self.step_times[step] = step_time + self.step_times.get(step, 0.0)

        return wrapped_ctx()

    def write_logs(self, task: TaskT, model: ModelT, state: State) -> None:
        for step, step_time in self.step_times.items():
            self.logger.log_scalar(step, step_time, namespace="⏰ dt")

        super().write_logs(task, model, state)

        # Empty step times when done, so we only log the current step times.
        self.step_times.clear()

    def on_profiler_trace_ready(self, prof: torch.profiler.profile) -> None:
        key_averages = prof.key_averages()

        # Prints a table with informative statistics.
        keys = ["self_cpu_time_total", "cpu_time_total", "cpu_memory_usage"]
        if torch.cuda.is_available():
            keys += ["self_cuda_time_total", "cuda_time_total", "cuda_memory_usage"]
        for key in keys:
            table = key_averages.table(
                sort_by=key,
                row_limit=self.config.profiler.table_size,
                top_level_events_only=False,
            )
            logger.info("%s:\n%s", key, table)

        # Saves a stack trace that is viewable in Chrome, in chrome://tracing/
        profile_dir = self.exp_dir / "profile"
        profile_dir.mkdir(exist_ok=True, parents=True)
        date_str = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        prof.export_chrome_trace(str(profile_dir / f"trace.step_{prof.step_num}.{date_str}.json"))

    def get_profile(self) -> torch.profiler.profile | None:
        if not self.config.profiler.enabled:
            return None

        if torch.cuda.is_available():
            profiler_activities = [
                torch.autograd.ProfilerActivity.CPU,
                torch.autograd.ProfilerActivity.CUDA,
            ]
        else:
            profiler_activities = [
                torch.autograd.ProfilerActivity.CPU,
            ]

        return torch.profiler.profile(
            activities=profiler_activities,
            record_shapes=self.config.profiler.record_shapes,
            profile_memory=self.config.profiler.profile_memory,
            with_stack=self.config.profiler.with_stack,
            with_flops=self.config.profiler.with_flops,
            with_modules=self.config.profiler.with_modules,
            schedule=torch.profiler.schedule(
                wait=self.config.profiler.wait_steps,
                warmup=self.config.profiler.warmup_steps,
                active=self.config.profiler.active_steps,
                repeat=self.config.profiler.repeat_steps,
                skip_first=self.config.profiler.skip_first_steps,
            ),
            on_trace_ready=self.on_profiler_trace_ready,
        )
