"""Defines a trainer to use for supervised learning.

This trainer is akin to PyTorch Lightning or Keras, in that it handles
the training loop, logging, and checkpointing. We get a dataset and dataloader
from the task, and then train the model on the dataset.
"""

import bisect
import contextlib
import functools
import itertools
import logging
import signal
from dataclasses import dataclass
from types import FrameType
from typing import Generic, Iterator, TypeVar

from omegaconf import MISSING

from ml.core.common_types import Batch
from ml.core.config import conf_field
from ml.core.registry import register_trainer
from ml.core.state import State
from ml.lr_schedulers.base import BaseLRScheduler
from ml.models.gan import GenerativeAdversarialNetworkModel
from ml.optimizers.base import BaseOptimizer
from ml.tasks.gan.base import GenerativeAdversarialNetworkTask
from ml.tasks.gan.round_robin import GenerativeAdversarialNetworkRoundRobinTask
from ml.tasks.sl.base import SupervisedLearningTask
from ml.trainers.base import ModelT
from ml.trainers.learning import BaseLearningTrainer, BaseLearningTrainerConfig
from ml.utils.containers import recursive_chunk
from ml.utils.device.base import InfinitePrefetcher
from ml.utils.exceptions import EpochDoneError, TrainingFinishedError
from ml.utils.timer import Timer

logger: logging.Logger = logging.getLogger(__name__)


@dataclass
class ValidationConfig:
    valid_every_n_steps: int | None = conf_field(None, help="Number of training steps to run per validation step")
    valid_every_n_seconds: float | None = conf_field(60.0 * 10.0, help="Run validation every N seconds")
    valid_first_n_seconds: float | None = conf_field(60.0, help="Run first validation after N seconds")


@dataclass
class BatchScheduleConfig:
    num_steps: int = conf_field(MISSING, help="Number of steps to run for")
    num_batches: int = conf_field(MISSING, help="Number of minibatches for a given step")


@dataclass
class SupervisedLearningTrainerConfig(BaseLearningTrainerConfig):
    validation: ValidationConfig = conf_field(ValidationConfig())
    batches_per_step: int = conf_field(1, help="Batches per training step, to simulate larger effective batch sizes")
    batches_per_step_schedule: list[BatchScheduleConfig] | None = conf_field(
        None,
        help="A schedule for the number of minibatches per step, as a list of (step_count, num_batches) tuples.",
    )
    batch_chunks_per_step_schedule: list[BatchScheduleConfig] | None = conf_field(
        None,
        help="A schedule for chunking the batches, as a list of (step_count, num_chunks) tuples.",
    )
    batch_dim: int = conf_field(0, help="The batch dimension, for splitting batches into chunks")


SupervisedLearningTrainerConfigT = TypeVar("SupervisedLearningTrainerConfigT", bound=SupervisedLearningTrainerConfig)
SupervisedLearningTaskT = TypeVar("SupervisedLearningTaskT", bound=SupervisedLearningTask)


@register_trainer("sl", SupervisedLearningTrainerConfig)
class SupervisedLearningTrainer(
    BaseLearningTrainer[SupervisedLearningTrainerConfigT, ModelT, SupervisedLearningTaskT],
    Generic[SupervisedLearningTrainerConfigT, ModelT, SupervisedLearningTaskT],
):
    def __init__(self, config: SupervisedLearningTrainerConfigT) -> None:
        super().__init__(config)

        self.last_valid_time: float | None = None
        self.last_valid_step: int | None = None
        self.first_valid_step_flag = True

    @functools.lru_cache()
    def batches_per_step_schedule(self) -> list[tuple[int, int]] | None:
        schedule = self.config.batches_per_step_schedule
        if schedule is None:
            return None
        if any(s.num_steps <= 0 or s.num_batches <= 0 for s in schedule):
            raise ValueError("steps and num_batches must be non-negative")
        schedule_list = [(s.num_steps, s.num_batches) for s in schedule]
        schedule_cumsum = list(itertools.accumulate([0] + [s[0] for s in schedule_list]))
        return list(zip(schedule_cumsum[1:], [s[1] for s in schedule_list]))

    def get_batches_per_step(self, state: State) -> int:
        if (schedule := self.batches_per_step_schedule()) is None:
            return self.config.batches_per_step
        i = bisect.bisect_left(schedule, (state.num_steps, 0))
        return schedule[-1][1] if i == len(schedule) else schedule[i][1]

    @functools.lru_cache()
    def batch_chunks_schedule(self) -> list[tuple[int, int]] | None:
        schedule = self.config.batch_chunks_per_step_schedule
        if schedule is None:
            return None
        if any(s.num_steps <= 0 or s.num_batches <= 0 for s in schedule):
            raise ValueError("steps and num_batches must be non-negative")
        schedule_list = [(s.num_steps, s.num_batches) for s in schedule]
        schedule_cumsum = list(itertools.accumulate([0] + [s[0] for s in schedule_list]))
        return list(zip(schedule_cumsum[1:], [s[1] for s in schedule_list]))

    def get_batch_chunks(self, state: State) -> int:
        if (schedule := self.batch_chunks_schedule()) is None:
            return 1
        i = bisect.bisect_left(schedule, (state.num_steps, 0))
        return 1 if i == len(schedule) else schedule[i][1]

    def should_validate(self, state: State) -> bool:
        if self.last_valid_time is None or self.last_valid_step is None:
            self.last_valid_time = state.elapsed_time_s
            self.last_valid_step = state.num_steps
            return True

        # Step-based validation.
        valid_every_n_steps = self.config.validation.valid_every_n_steps
        if valid_every_n_steps is not None and state.num_steps > valid_every_n_steps + self.last_valid_step:
            self.last_valid_step = state.num_steps
            return True

        # Time-based validation.
        valid_every_n_seconds = self.config.validation.valid_every_n_seconds
        if valid_every_n_seconds is not None and state.elapsed_time_s - self.last_valid_time >= valid_every_n_seconds:
            self.last_valid_time = state.elapsed_time_s
            return True

        # Time-based validation for first validation step.
        if self.first_valid_step_flag:
            valid_first_n_seconds = self.config.validation.valid_first_n_seconds
            if valid_first_n_seconds is not None and state.elapsed_time_s >= valid_first_n_seconds:
                self.last_valid_time = state.elapsed_time_s
                self.first_valid_step_flag = False
                return True

        return False

    def train(
        self,
        model: ModelT,
        task: SupervisedLearningTaskT,
        optimizer: BaseOptimizer,
        lr_scheduler: BaseLRScheduler,
    ) -> None:
        """Runs the training loop.

        Args:
            model: The current model
            task: The current task
            optimizer: The current optimizer
            lr_scheduler: The current learning rate scheduler

        Raises:
            ValueError: If the task is not a supervised learning task
        """
        if not isinstance(task, SupervisedLearningTask):
            raise ValueError(f"Expected task to be a SupervisedLearningTask, got {type(task)}")
        if isinstance(model, GenerativeAdversarialNetworkModel):
            raise ValueError("Model is a GenerativeAdversarialNetworkModel, use `gan` trainer instead")
        if isinstance(task, (GenerativeAdversarialNetworkTask, GenerativeAdversarialNetworkRoundRobinTask)):
            raise ValueError("Task is a GenerativeAdversarialNetworkTask, use `gan` trainer instead")

        self._init_environment()

        with Timer("compiling model"):
            model = self._compile_model(model)

        with Timer("compiling training step"):
            train_step = self._compile_func(self.train_step)

        with Timer("compiling validation step"):
            val_step = self._compile_func(self.val_step)

        with Timer("building task model"):
            task_model = self._get_task_model(task, model)

        optim, lr_sched = self._get_optim_and_lr_sched(task_model, optimizer, lr_scheduler)
        state = self._get_state(task, model, optim, lr_sched)

        def on_exit(signum: int, _: FrameType | None) -> None:
            sig = signal.Signals(signum)
            self.on_exit(sig, state, task, model, optim, lr_sched)

        # Handle user-defined interrupts.
        signal.signal(signal.SIGUSR1, on_exit)

        # Gets the datasets.
        with Timer("getting datasets", 0.1):
            train_ds = task.get_dataset("train")
            valid_ds = task.get_dataset("valid")

        # Gets the dataloaders.
        with Timer("getting dataloaders", 0.1):
            train_dl = task.get_dataloader(train_ds, "train")
            valid_dl = task.get_dataloader(valid_ds, "valid")

        # Gets the prefetchers.
        with Timer("getting prefetchers", 0.1):
            train_pf = self._device.get_prefetcher(train_dl)
            valid_pf = self._device.get_prefetcher(valid_dl)
            valid_pf_iter = iter(InfinitePrefetcher(valid_pf))

        self.on_training_start(state, task, model, optim, lr_sched)

        try:
            with contextlib.ExitStack() as ctx:
                profile = self.get_profile()
                if profile is not None:
                    ctx.enter_context(profile)

                while True:
                    with self.step_context("on_epoch_start"):
                        self.on_epoch_start(state, task, model, optim, lr_sched)

                    def batch_splitter() -> Iterator[Batch]:
                        num_chunks = self.get_batch_chunks(state)
                        for batch in train_pf:
                            yield from recursive_chunk(batch, num_chunks, dim=self.config.batch_dim)

                    train_pf_iter: Iterator = batch_splitter()

                    def batch_iterator() -> Iterator[Batch]:
                        try:
                            yield next(train_pf_iter)
                        except StopIteration:
                            raise EpochDoneError

                        for _ in range(self.get_batches_per_step(state) - 1):
                            try:
                                yield next(train_pf_iter)
                            except StopIteration:
                                pass

                    while True:
                        if self.should_validate(state):
                            self._log_prefetcher_stats(valid_pf)

                            val_step(
                                task_model=task_model,
                                batch=next(valid_pf_iter),
                                state=state,
                                task=task,
                                model=model,
                            )

                        self._log_prefetcher_stats(train_pf)

                        if task.is_training_over(state):
                            raise TrainingFinishedError

                        with self.step_context("on_step_start"):
                            self.on_step_start(state, task, model, optim, lr_sched)

                        try:
                            loss_dict = train_step(
                                task_model=task_model,
                                batches=batch_iterator(),
                                state=state,
                                task=task,
                                model=model,
                                optim=optim,
                                lr_sched=lr_sched,
                            )

                        except EpochDoneError:
                            break

                        if self.should_checkpoint(state):
                            self.save_checkpoint(state, task, model, optim, lr_sched)

                        if profile is not None:
                            profile.step()

                        with self.step_context("on_step_end"):
                            self.on_step_end(state, loss_dict, task, model, optim, lr_sched)

                    with self.step_context("on_epoch_end"):
                        self.on_epoch_end(state, task, model, optim, lr_sched)

        except TrainingFinishedError:
            self.save_checkpoint(state, task, model, optim, lr_sched)
            logger.info(
                "Finished training after %d epochs, %d steps, %d samples",
                state.num_epochs,
                state.num_steps,
                state.num_samples,
            )

        except Exception:
            logger.exception("Caught exception during training loop for %s", self.config_path)

        finally:
            self.on_training_end(state, task, model, optim, lr_sched)
