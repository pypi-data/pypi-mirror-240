"""Defines the base logger.

New loggers should implement whichever `log_` functions they need to.
Unimplemented functions are simply ignored. The framework will handle logging
rate limiting and munging the logged values to a common format.

The internal ergonomics for logging are a bit confusing to follow. Each
component has access to a ``MultiLogger`` which it can use to log values.
After each step, each ``MultiLogger`` sends its values to any implemented
loggers which have ``should_write`` return ``True``. This lets the implemented
loggers aggregate values over multiple ``MultiLogger``s. New loggers should
follow the implementation of one of the existing loggers.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Generic, TypeVar, Union

from omegaconf import DictConfig
from torch import Tensor

from ml.core.config import BaseConfig, BaseObject, conf_field
from ml.core.state import Phase, State

Number = Union[int, float, Tensor]


@dataclass
class BaseLoggerConfig(BaseConfig):
    write_every_n_seconds: float | None = conf_field(None, help="Only write a log line every N seconds")
    write_train_every_n_seconds: float | None = conf_field(None, help="Only write a train log line every N seconds")
    write_val_every_n_seconds: float | None = conf_field(None, help="Only write a val log line every N seconds")


LoggerConfigT = TypeVar("LoggerConfigT", bound=BaseLoggerConfig)


class BaseLogger(BaseObject[LoggerConfigT], Generic[LoggerConfigT], ABC):
    """Defines the base logger."""

    log_directory: Path

    def __init__(self, config: LoggerConfigT) -> None:
        super().__init__(config)

        self.last_write_time: dict[Phase, float] = {}

    def initialize(self, log_directory: Path) -> None:
        self.log_directory = log_directory

    def log_scalar(self, key: str, value: Callable[[], Number], state: State, namespace: str) -> None:
        """Logs a scalar value.

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_string(self, key: str, value: Callable[[], str], state: State, namespace: str) -> None:
        """Logs a string value.

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_image(self, key: str, value: Callable[[], Tensor], state: State, namespace: str) -> None:
        """Logs a normalized image, with shape (C, H, W).

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_audio(self, key: str, value: Callable[[], tuple[Tensor, int]], state: State, namespace: str) -> None:
        """Logs a normalized audio, with shape (T,).

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_video(self, key: str, value: Callable[[], Tensor], state: State, namespace: str) -> None:
        """Logs a normalized video, with shape (T, C, H, W).

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_histogram(self, key: str, value: Callable[[], Tensor], state: State, namespace: str) -> None:
        """Logs a histogram, with any shape.

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_point_cloud(self, key: str, value: Callable[[], Tensor], state: State, namespace: str) -> None:
        """Logs a normalized point cloud, with shape (B, N, 3).

        Args:
            key: The key to log
            value: The value to log
            state: The current log state
            namespace: The namespace to be logged
        """

    def log_config(self, config: DictConfig) -> None:
        """Logs a set of metrics and configuration.

        This is only called once, when metrics are computed for a whole dataset.

        Args:
            config: The run config
        """

    def should_write(self, state: State) -> bool:
        """Returns whether or not the current state should be written.

        This function checks that the last time the current phase was written
        was greater than some interval in the past, to avoid writing tons of
        values when the iteration time is extremely small.

        Args:
            state: The state to check

        Returns:
            If the logger should write values for the current state
        """
        if state.phase not in self.last_write_time:
            self.last_write_time[state.phase] = state.elapsed_time_s
            return True
        elif state.elapsed_time_s - self.last_write_time[state.phase] < self.write_every_n_seconds(state):
            return False
        else:
            self.last_write_time[state.phase] = state.elapsed_time_s
            return True

    @abstractmethod
    def write(self, state: State) -> None:
        """Writes the logs.

        Args:
            state: The current log state
        """

    @abstractmethod
    def default_write_every_n_seconds(self, state: State) -> float:
        """Returns the default write interval in seconds.

        Args:
            state: The state to get the default write interval for

        Returns:
            The default write interval, in seconds
        """

    def write_every_n_seconds(self, state: State) -> float:
        """Returns the write interval in seconds.

        Args:
            state: The state to get the write interval for

        Returns:
            The write interval, in seconds
        """
        if state.phase == "train":
            if self.config.write_train_every_n_seconds is not None:
                return self.config.write_train_every_n_seconds
        elif self.config.write_val_every_n_seconds is not None:
            return self.config.write_val_every_n_seconds

        if self.config.write_every_n_seconds is not None:
            return self.config.write_every_n_seconds

        return self.default_write_every_n_seconds(state)
