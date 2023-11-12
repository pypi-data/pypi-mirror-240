# pylint: disable=too-many-public-methods
"""Defines the base class and config for all tasks.

Tasks are the main unit of work in the ML framework. They are responsible for
defining the training, validation, and testing loops, as well as data loading,
logging, and model evaluation. They also do a lot of timing and logging of
performance metrics, with some hooks for calling custom code snippets at
various points. Typically, you should use either the
:class:`ml.tasks.sl.SupervisedLearningTask` or
:class:`ml.tasks.rl.ReinforcementLearningTask` classes instead of this base
class.
"""

import functools
import logging
import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, is_dataclass
from pathlib import Path
from typing import Any, Generic, Mapping, Sequence, Sized, TypeVar

import numpy as np
import torch
from omegaconf import II, MISSING, OmegaConf
from torch import Tensor, nn
from torch.optim.optimizer import Optimizer
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.datapipes.datapipe import IterDataPipe, MapDataPipe
from torch.utils.data.dataset import Dataset
from torch.utils.data.sampler import Sampler

from ml.core.common_types import Batch, Loss, Output
from ml.core.config import BaseConfig, BaseObject, conf_field
from ml.core.env import is_debugging
from ml.core.state import Phase, State
from ml.loggers.multi import MultiLogger
from ml.lr_schedulers.base import SchedulerAdapter
from ml.models.base import BaseModel
from ml.tasks.datasets.collate import CollateMode, collate
from ml.tasks.datasets.error_handling import (
    ErrorHandlingConfig,
    error_handling_dataset,
)
from ml.utils.colors import make_bold
from ml.utils.device.auto import detect_device
from ml.utils.device.base import base_device
from ml.utils.random import set_random_seed

logger: logging.Logger = logging.getLogger(__name__)

DataPipeT = TypeVar("DataPipeT", bound=IterDataPipe | MapDataPipe)

PRINT_FINISH_TIME_EVERY_N_SECONDS = 60 * 2


def num_workers(default: int) -> int:
    if (cpu_count := os.cpu_count()) is None:
        return default
    # This is a somewhat arbitrary heuristic, but seems to be a fine default.
    return min(cpu_count * 2, 8)


OmegaConf.register_new_resolver("ml.num_workers", num_workers, replace=True)


class CumulativeTimer:
    """Defines a simple timer to track an average value."""

    def __init__(self) -> None:
        self.steps = 0
        self.elapsed_time = 0.0

    @functools.cached_property
    def start_time(self) -> float:
        return time.time()

    def step(self, steps: int, cur_time: float) -> None:
        if steps != self.steps:
            self.steps = steps
            self.elapsed_time = cur_time - self.start_time

    @property
    def steps_per_second(self) -> float:
        return 0.0 if self.elapsed_time < 1e-4 else self.steps / self.elapsed_time

    @property
    def steps_per_hour(self) -> float:
        return self.steps_per_second * 60 * 60

    @property
    def seconds_per_step(self) -> float:
        return 0.0 if self.steps <= 0 else self.elapsed_time / self.steps

    @property
    def hours_per_step(self) -> float:
        return self.seconds_per_step / (60 * 60)


class IterationTimer:
    """Defines a simple timer to track consecutive values."""

    def __init__(self) -> None:
        self.iteration_time = 0.0
        self.last_time = time.time()

    def step(self, cur_time: float) -> None:
        self.iteration_time = cur_time - self.last_time
        self.last_time = cur_time

    @property
    def iter_seconds(self) -> float:
        return self.iteration_time

    @property
    def iter_hours(self) -> float:
        return self.iter_seconds / (60 * 60)


class StateTimer:
    """Defines a timer for all state information."""

    def __init__(self) -> None:
        self.epoch_timer = CumulativeTimer()
        self.step_timer = CumulativeTimer()
        self.sample_timer = CumulativeTimer()
        self.iter_timer = IterationTimer()

    def step(self, state: State) -> None:
        cur_time = time.time()
        self.epoch_timer.step(state.num_epochs, cur_time)
        self.step_timer.step(state.num_steps, cur_time)
        self.sample_timer.step(state.num_samples, cur_time)
        self.iter_timer.step(cur_time)

    def log_dict(self) -> dict[str, dict[str, int | float]]:
        logs: dict[str, dict[str, int | float]] = {}

        # Logs epoch statistics (only if at least one epoch seen).
        if self.epoch_timer.steps > 0:
            logs["⏰ epoch"] = {
                "total": self.epoch_timer.steps,
                "hours-per": self.epoch_timer.steps_per_hour,
            }

        # Logs step statistics.
        logs["⏰ steps"] = {
            "total": self.step_timer.steps,
            "per-second": self.step_timer.steps_per_second,
            "per-hour": self.step_timer.steps_per_hour,
        }

        # Logs sample statistics.
        logs["⏰ samples"] = {
            "total": self.sample_timer.steps,
            "per-second": self.sample_timer.steps_per_second,
            "per-hour": self.sample_timer.steps_per_hour,
        }

        # Logs full iteration statistics.
        logs["⏰ dt"] = {
            "iter": self.iter_timer.iter_seconds,
        }

        return logs


@dataclass
class DataLoaderConfig:
    batch_size: int = conf_field(MISSING, help="Size of each batch")
    batch_size_multiplier: float = conf_field(MISSING, help="Batch size multiplier")
    shuffle: bool = conf_field(MISSING, help="Should the batches be shuffled on each iteration")
    num_workers: int = conf_field(MISSING, help="Number of workers for loading samples")
    pin_memory: bool = conf_field(MISSING, help="Should memory be pinned to it's GPU location")
    drop_last: bool = conf_field(MISSING, help="Should the last batch be dropped if not full")
    timeout: float = conf_field(0, help="How long to wait for a sample to be ready")
    prefetch_factor: int | None = conf_field(None, help="Number of items to pre-fetch on each worker")
    persistent_workers: bool = conf_field(False, help="Persist worker processes between epochs")
    seed: int = conf_field(1337, help="Dataloader random seed")


@dataclass
class DataLoaderConfigs:
    train_dl: DataLoaderConfig = conf_field(
        DataLoaderConfig(
            batch_size_multiplier=1.0,
            shuffle=True,
            num_workers=II("ml.num_workers:8"),
            pin_memory=True,
            drop_last=True,
            persistent_workers=True,
        ),
        help="Train dataloader config",
    )
    valid_dl: DataLoaderConfig = conf_field(
        DataLoaderConfig(
            batch_size=II("task.train_dl.batch_size"),
            batch_size_multiplier=II("task.train_dl.batch_size_multiplier"),
            shuffle=True,
            num_workers=0,
            pin_memory=False,
            drop_last=False,
            persistent_workers=False,
        ),
        help="Valid dataloader config",
    )
    test_dl: DataLoaderConfig = conf_field(
        DataLoaderConfig(
            batch_size=II("task.valid_dl.batch_size"),
            batch_size_multiplier=II("task.valid_dl.batch_size_multiplier"),
            shuffle=False,
            num_workers=0,
            pin_memory=False,
            drop_last=False,
            persistent_workers=False,
        ),
        help="Test dataloader config",
    )


@dataclass
class FinishTrainingConfig:
    max_epochs: int | None = conf_field(None, help="Maximum number of epochs to run")
    max_steps: int | None = conf_field(None, help="Maximum number of steps to run")
    max_samples: int | None = conf_field(None, help="Maximum number of samples to run")
    max_seconds: float | None = conf_field(None, help="Maximum number of seconds to run")


@dataclass
class BaseTaskConfig(BaseConfig, DataLoaderConfigs, FinishTrainingConfig):
    """Defines the base config for all tasks."""

    errors: ErrorHandlingConfig = conf_field(ErrorHandlingConfig(), help="Error handling config")


BaseTaskConfigT = TypeVar("BaseTaskConfigT", bound=BaseTaskConfig)
ModelT = TypeVar("ModelT", bound=BaseModel)


class BaseTask(
    nn.Module,
    BaseObject[BaseTaskConfigT],
    Generic[BaseTaskConfigT, ModelT, Batch, Output, Loss],
    ABC,
):
    """Defines the base task type."""

    def __init__(self, config: BaseTaskConfigT) -> None:
        nn.Module.__init__(self)
        BaseObject.__init__(self, config)

        self.dataloader_configs: dict[Phase, DataLoaderConfig] = {
            "train": self.config.train_dl,
            "valid": self.config.valid_dl,
            "test": self.config.test_dl,
        }

        # This flag can be toggled to end training from anywhere in the task.
        self.__training_over_flag = False

        # This flag is used for printing the estimated termination time.
        self.__last_printed_remaining_time = 0.0

        # Timers for iterations.
        self.train_timer = StateTimer()
        self.valid_timer = StateTimer()
        self.test_timer = StateTimer()

        # Used to log values.
        self.logger = MultiLogger(default_namespace="task")

        # Gets the device and device type.
        self._device = self._get_device()
        self._device_type = self._get_device_type()

    @torch.jit.ignore
    def _get_device(self) -> base_device:
        return detect_device()

    @torch.jit.ignore
    def _get_device_type(self) -> str:
        return self._device._get_device().type

    @abstractmethod
    def run_model(self, model: ModelT, batch: Batch, state: State) -> Output:
        """Runs a single training step and returns the outputs.

        Args:
            model: The current nn.Module
            batch: The current batch
            state: The current trainer state

        Returns:
            The outputs from the model
        """

    @abstractmethod
    def compute_loss(self, model: ModelT, batch: Batch, state: State, output: Output) -> Loss:
        """Computes the loss for a given output.

        If the loss is a tensor, it should have shape (B). If the loss is a
        dictionary of tensors, each tensor should have the same shape (B).

        Args:
            model: The current nn.Module
            batch: The current batch
            state: The current trainer state
            output: The model output from `run_model`

        Returns:
            The computed loss, as a tensor or dictionary of tensors
        """

    def get_single_loss(self, loss: Loss) -> tuple[Tensor, list[str]]:
        """Combines the output losses to get a single loss with shape (N, B).

        Args:
            loss: The computed loss or losses, either a tensor or dictionary of
                tensors. If a dictionary, all loss tensors need to have the
                same shape.

        Returns:
            The single loss with shape (N), where N is the number of losses,
            and the loss names, a list of length N.
        """
        if isinstance(loss, Tensor):
            if loss.ndim == 0:
                return loss.unsqueeze(0), ["loss"]
            if loss.ndim == 1:
                return loss, ["loss"]
            return loss.sum().unsqueeze(0) / loss.shape[0], ["loss"]
        assert isinstance(loss, dict), f"Loss should be a scalar or dictionary, not {type(loss)}"
        keys, values = (list(i) for i in zip(*sorted(loss.items())))
        losses = [v.sum() / v.shape[0] if v.ndim > 0 else v for v in values]
        single_loss = torch.stack(losses, dim=0)
        return single_loss, keys

    def log_loss_dict(self, loss: Mapping[str, int | float | Tensor], state: State) -> None:
        for k, v in loss.items():
            self.logger.log_scalar(k, v, namespace="loss")

        match state.phase:
            case "train":
                timer = self.train_timer
            case "valid":
                timer = self.valid_timer
            case "test":
                timer = self.test_timer
            case _:
                raise NotImplementedError(f"Unexpected phase: {state.phase}")

        timer.step(state)
        for ns, d in timer.log_dict().items():
            for k, v in d.items():
                self.logger.log_scalar(k, v, namespace=ns)

    def get_batch_size(self, batch: Batch) -> int | None:
        if isinstance(batch, (np.ndarray, Tensor)):
            return batch.shape[0]
        if is_dataclass(batch):
            for v in batch.__dict__.values():
                if bsz := self.get_batch_size(v):
                    return bsz
        if isinstance(batch, Mapping):
            for v in batch.values():
                if bsz := self.get_batch_size(v):
                    return bsz
        if isinstance(batch, Sequence):
            for i in batch:
                if bsz := self.get_batch_size(i):
                    return bsz
        return None

    def set_training_over(self) -> None:
        self.__training_over_flag = True

    def maybe_log_termination_time(self, remaining_percent: float, state: State) -> None:
        if self.__last_printed_remaining_time + PRINT_FINISH_TIME_EVERY_N_SECONDS > state.elapsed_time_s:
            return
        self.__last_printed_remaining_time = state.elapsed_time_s
        remaining_seconds = remaining_percent * state.elapsed_time_s / (1 - remaining_percent)
        termination_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + remaining_seconds))
        info_str = f"Training over: {termination_time}"
        logger.info("Estimated training finish time:\n%s", make_bold([info_str], "light-cyan", "blue"))

    def get_remaining_percent(self, state: State) -> float | None:
        remaining_percents: list[float] = []
        if self.config.max_epochs is not None:
            remaining_percents.append((self.config.max_epochs - state.num_epochs) / self.config.max_epochs)
        if self.config.max_steps is not None:
            remaining_percents.append((self.config.max_steps - state.num_steps) / self.config.max_steps)
        if self.config.max_samples is not None:
            remaining_percents.append((self.config.max_samples - state.num_samples) / self.config.max_samples)
        if self.config.max_seconds is not None:
            remaining_percents.append((self.config.max_seconds - state.elapsed_time_s) / self.config.max_seconds)
        return None if len(remaining_percents) == 0 else min(remaining_percents)

    def is_training_over(self, state: State) -> bool:
        if self.__training_over_flag:
            return True
        remaining_percent = self.get_remaining_percent(state)
        if remaining_percent is None:
            return False
        self.logger.log_scalar("percent", remaining_percent, namespace="⏰ remaining")
        self.maybe_log_termination_time(remaining_percent, state)
        return remaining_percent <= 0.0

    def get_sampler(self, dataset: Dataset, cfg: DataLoaderConfig, phase: Phase) -> Sampler[int]:
        """Returns a dataset sampler to use instead of random sampling.

        The default behavior for a non-iterable dataset is to use a
        RandomSampler for all the elements from the dataset. The sampler
        should yield integer indices into the dataset.

        Args:
            dataset: The dataset to sample from
            cfg: The associated dataloader config
            phase: The dataset's phase

        Raises:
            NotImplementedError: If this method is not overridden
        """
        raise NotImplementedError("`get_sampler` should be implemented for the specific task")

    def get_batch_sampler(self, sampler: Sampler, cfg: DataLoaderConfig, phase: Phase) -> Sampler[list[int]]:
        """Returns a dataset batch sampler to use instead fo sequential sampling.

        The batch sampler should yield lists of integer indices, which
        are the samples that are passed to the dataset.

        Args:
            sampler: The underlying sampler
            cfg: The associated dataloader config
            phase: The dataset's phase

        Raises:
            NotImplementedError: If this method is not overridden
        """
        raise NotImplementedError("`get_sampler` should be implemented for the specific task")

    def apply_datapipe_transformations(self, datapipe: DataPipeT, phase: Phase) -> DataPipeT:
        """Applies transformations to the datapipe.

        Args:
            datapipe: The datapipe to transform
            phase: The dataset's phase

        Returns:
            The transformed datapipe
        """
        if phase not in self.dataloader_configs:
            raise KeyError(f"Missing {phase=} in dataloader configs")
        cfg = self.dataloader_configs[phase]

        # Wraps the dataset in an error-handling dataset.
        if self.config.errors.enabled:
            datapipe = error_handling_dataset(datapipe, self.config.errors)

        datapipe = datapipe.shuffle() if phase == "train" else datapipe
        datapipe = datapipe.sharding_filter()
        datapipe = datapipe.batch(round(cfg.batch_size * cfg.batch_size_multiplier), drop_last=cfg.drop_last)
        datapipe = datapipe.collate(collate_fn=self.collate_fn)

        return datapipe

    def get_datapipe_dataloader(self, datapipe: MapDataPipe | IterDataPipe, phase: Phase) -> DataLoader:
        debugging = is_debugging()
        if debugging:
            logger.warning("Parallel dataloaders disabled in debugging mode")

        if phase not in self.dataloader_configs:
            raise KeyError(f"Missing {phase=} in dataloader configs")
        cfg = self.dataloader_configs[phase]

        datapipe = self.apply_datapipe_transformations(datapipe, phase)

        return DataLoader(
            datapipe,
            num_workers=0 if debugging else cfg.num_workers,
            pin_memory=cfg.pin_memory,
            timeout=0 if debugging else cfg.timeout,
            worker_init_fn=self.worker_init_fn,
            multiprocessing_context=None,
            generator=None,
            prefetch_factor=None if debugging or cfg.num_workers == 0 else cfg.prefetch_factor,
            persistent_workers=False if debugging or cfg.num_workers == 0 else cfg.persistent_workers,
        )

    def get_dataloader(self, dataset: Dataset, phase: Phase) -> DataLoader:
        if isinstance(dataset, (MapDataPipe, IterDataPipe)):
            return self.get_datapipe_dataloader(dataset, phase)

        debugging = is_debugging()
        if debugging:
            logger.warning("Parallel dataloaders disabled in debugging mode")

        if phase not in self.dataloader_configs:
            raise KeyError(f"Missing {phase=} in dataloader configs")
        cfg = self.dataloader_configs[phase]

        # Wraps the dataset in an error-handling dataset.
        if self.config.errors.enabled:
            dataset = error_handling_dataset(dataset, self.config.errors)

        # Arguments shared by all dataloaders.
        common_kwargs = {
            "num_workers": 0 if debugging else cfg.num_workers,
            "collate_fn": self.collate_fn,
            "pin_memory": cfg.pin_memory,
            "timeout": 0 if debugging else cfg.timeout,
            "worker_init_fn": self.worker_init_fn,
            "multiprocessing_context": None,
            "generator": None,
            "prefetch_factor": None if debugging or cfg.num_workers == 0 else cfg.prefetch_factor,
            "persistent_workers": False if debugging or cfg.num_workers == 0 else cfg.persistent_workers,
        }

        try:
            sampler = self.get_sampler(dataset, cfg, phase)
        except NotImplementedError:
            return DataLoader(
                dataset=dataset,
                batch_size=round(cfg.batch_size * cfg.batch_size_multiplier),
                drop_last=cfg.drop_last,
                shuffle=cfg.shuffle if isinstance(dataset, Sized) else False,
                **common_kwargs,  # type: ignore[arg-type]
            )

        try:
            batch_sampler = self.get_batch_sampler(sampler, cfg, phase)
        except NotImplementedError:
            return DataLoader(
                dataset=dataset,
                sampler=sampler,
                batch_size=round(cfg.batch_size * cfg.batch_size_multiplier),
                drop_last=cfg.drop_last,
                **common_kwargs,  # type: ignore[arg-type]
            )

        return DataLoader(
            dataset=dataset,
            batch_sampler=batch_sampler,
            **common_kwargs,  # type: ignore[arg-type]
        )

    @classmethod
    def worker_init_fn(cls, worker_id: int) -> None:
        set_random_seed(offset=worker_id)

    @classmethod
    def collate_fn(cls, items: list[Any], *, mode: CollateMode = "stack") -> Any | None:  # noqa: ANN401
        return collate(items, mode=mode)

    # -----
    # Hooks
    # -----

    def on_after_save_checkpoint(self, ckpt_path: Path) -> None:
        pass

    def on_before_forward_step(self, model: ModelT, batch: Batch, state: State) -> None:
        pass

    def on_after_forward_step(self, model: ModelT, batch: Batch, output: Output, state: State) -> None:
        pass

    def on_after_compute_loss(self, model: ModelT, batch: Batch, output: Output, loss: Loss, state: State) -> None:
        pass

    def on_step_start(
        self,
        state: State,
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass

    def on_step_end(
        self,
        state: State,
        loss_dict: dict[str, Tensor],
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass

    def on_epoch_start(
        self,
        state: State,
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass

    def on_epoch_end(
        self,
        state: State,
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass

    def on_training_start(
        self,
        state: State,
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass

    def on_training_end(
        self,
        state: State,
        model: ModelT,
        optim: Optimizer | dict[str, Optimizer],
        lr_sched: SchedulerAdapter | dict[str, SchedulerAdapter],
    ) -> None:
        pass
