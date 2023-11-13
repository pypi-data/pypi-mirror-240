"""Defines a linear warmup and decay learning rate scheduler.

This scheduler first warms up some number of steps, then smoothly decays
until the end of training.
"""

from dataclasses import dataclass

from omegaconf import II, MISSING, OmegaConf

from ml.core.config import conf_field
from ml.core.registry import register_lr_scheduler
from ml.core.state import State
from ml.lr_schedulers.base import BaseLRScheduler, BaseLRSchedulerConfig


@dataclass
class LinearLRSchedulerConfig(BaseLRSchedulerConfig):
    warmup_steps: int = conf_field(MISSING, help="Number of warmup steps")
    total_steps: int = conf_field(II("task.max_steps"), help="Total number of steps to run")
    warmup_percent: float = conf_field(0.01, help="Percentage of total steps to use as warmup steps, if not specified")
    min_scale: float = conf_field(1e-4, help="Minimum learning rate scale")
    decay: bool = conf_field(True, help="Whether to decay the learning rate after warmup")

    @classmethod
    def resolve(cls, config: "LinearLRSchedulerConfig") -> None:
        if OmegaConf.is_missing(config, "warmup_steps"):
            config.warmup_steps = int(config.total_steps * config.warmup_percent)
        super().resolve(config)


@register_lr_scheduler("linear", LinearLRSchedulerConfig)
class LinearLRScheduler(BaseLRScheduler[LinearLRSchedulerConfig]):
    def get_lr_scale(self, state: State) -> float:
        warmup, total, min_scale = self.config.warmup_steps, self.config.total_steps, self.config.min_scale
        if state.num_steps < warmup:
            return state.num_steps / warmup
        if not self.config.decay:
            return 1.0
        if state.num_steps < total:
            return (1 - min_scale) * (total - state.num_steps) / (total - warmup) + min_scale
        return min_scale
