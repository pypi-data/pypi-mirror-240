"""Defines error handling wrappers for datasets.

The worst feeling in the world is when you're training a model and it crashes
after 10 hours of training. This module defines some error handling wrappers
for datasets which will catch errors and log them (in batches).
"""

import bdb
import logging
import random
import sys
import time
from collections import Counter
from dataclasses import dataclass
from typing import Iterator, TypeVar, no_type_check

from torch.utils.data.datapipes._decorator import functional_datapipe
from torch.utils.data.datapipes.datapipe import IterDataPipe, MapDataPipe
from torch.utils.data.dataset import Dataset, IterableDataset

from ml.core.config import conf_field
from ml.utils.colors import colorize
from ml.utils.data import get_worker_info

logger: logging.Logger = logging.getLogger(__name__)

BatchT = TypeVar("BatchT")
DatasetT = TypeVar("DatasetT", Dataset, IterableDataset, MapDataPipe, IterDataPipe)


def get_loc(num_excs: int = 1) -> str:
    _, _, exc_tb = sys.exc_info()
    if exc_tb is None or (exc_tb := exc_tb.tb_next) is None:
        return "unknown"
    exc_strs: list[str] = []
    for _ in range(num_excs):
        exc_strs += [f"{exc_tb.tb_frame.f_code.co_filename}:{exc_tb.tb_lineno}"]
        if (exc_tb := exc_tb.tb_next) is None:
            break
    return "\n".join(exc_strs)


@dataclass
class ErrorHandlingConfig:
    enabled: bool = conf_field(True, help="Is error handling enabled?")
    maximum_exceptions: int = conf_field(10, help="Maximum number of errors to encounter")
    backoff_after: int = conf_field(5, help="Start to do a sleeping backoff after this many exceptions")
    sleep_backoff: float = conf_field(0.1, help="Sleep backoff amount")
    sleep_backoff_power: float = conf_field(2.0, help="How much to multiply backoff for each successive exception")
    log_full_exception: bool = conf_field(False, help="Log the full exception message for each exception")
    flush_exception_summary_every: int = conf_field(500, help="How often to flush exception summary")
    report_top_n_exception_types: int = conf_field(5, help="Number of exceptions to summarize")
    exception_location_traceback_depth: int = conf_field(3, help="Traceback length for the exception location")


class ExceptionSummary:
    def __init__(self, config: ErrorHandlingConfig) -> None:
        self.steps = 0
        self.step_has_error = False
        self.total_exceptions = 0
        self.flush_every = config.flush_exception_summary_every
        self.summary_length = config.report_top_n_exception_types
        self.exceptions: Counter[str] = Counter()
        self.exception_classes: Counter[str] = Counter()
        self.exception_locs: Counter[str] = Counter()
        self.last_exception: Exception | None = None

    def add_exception(self, exc: Exception, loc: str) -> None:
        self.last_exception = exc
        self.exceptions[f"{exc.__class__.__name__}: {exc}"] += 1
        self.exception_classes[exc.__class__.__name__] += 1
        self.exception_locs[loc] += 1
        if not self.step_has_error:
            self.total_exceptions += 1
            self.step_has_error = True

    def step(self) -> None:
        if self.steps >= self.flush_every:
            self.flush()
        self.steps += 1
        self.step_has_error = False

    def summary(self) -> str:
        lines: list[str] = []

        def get_segment_header(header: str) -> list[str]:
            header = colorize(f"{header:60s}", "yellow", bold=True)
            count = colorize(f"{'Count':10s}", "yellow", bold=False)
            percent = colorize(f"{'Percent':10s}", "yellow", bold=False)
            return [f"│ {header} │ {count} │ {percent} │"]

        def get_log_line(ks: str, v: int, as_red: bool = False) -> str:
            chunks = [k[i : i + 60] for k in ks.split("\n") for i in range(0, len(k), 60)]
            v_int, v_prct = f"{v}", f"{int(v * 100 / self.steps)} %"
            c = colorize(f"{chunks[0]:60s}", "red", bold=True) if as_red else f"{chunks[0]:60s}"
            log_lines = [f"│ {c} │ {v_int:10s} │ {v_prct:10s} │"]
            for chunk in chunks[1:]:
                c = colorize(f"{chunk:60s}", "red", bold=True) if as_red else f"{chunk:60s}"
                log_lines += [f"│ {c} │ {'':10s} │ {'':10s} │"]
            return "\n".join(log_lines)

        def get_single_log_line(ks: str) -> str:
            chunks = [k[i : i + 80] for k in ks.split("\n") for i in range(0, len(k), 82)]
            c = colorize(f"{chunks[0]:86s}", "red", bold=True)
            log_lines = [f"│ {c} │"]
            for chunk in chunks[1:]:
                c = colorize(f"{chunk:86s}", "red", bold=True)
                log_lines += [f"│ {c} │"]
            return "\n".join(log_lines)

        def get_line_break() -> str:
            return f"├─{'─' * 60}─┼─{'─' * 10}─┼─{'─' * 10}─┤"

        def get_line_start() -> str:
            return f"┌─{'─' * 60}─┬─{'─' * 10}─┬─{'─' * 10}─┐"

        def get_line_break_before_single() -> str:
            return f"├─{'─' * 60}─┴─{'─' * 10}─┴─{'─' * 10}─┤"

        def get_line_end() -> str:
            return f"└─{'─' * 60}───{'─' * 10}───{'─' * 10}─┘"

        # Logs the unique exception strings.
        lines += [get_line_start()]
        lines += get_segment_header("Error Messages")
        for k, v in self.exceptions.most_common(self.summary_length):
            lines += [get_log_line(k, v)]

        # Logs the individual exception classes.
        lines += [get_line_break()]
        lines += get_segment_header("Error Types")
        for k, v in self.exception_classes.most_common(self.summary_length):
            lines += [get_log_line(k, v)]

        # Logs by line number.
        lines += [get_line_break()]
        lines += get_segment_header("Error Locations")
        for k, v in self.exception_locs.most_common(self.summary_length):
            lines += [get_log_line(k, v)]

        # Logs the total number of exceptions.
        error_line = (
            f"Error Rate: {self.total_exceptions} failed / {self.steps} total "
            f"({self.total_exceptions / self.steps * 100:.2f} %)"
        )
        lines += [get_line_break_before_single()]
        lines += [get_single_log_line(error_line)]
        lines += [get_line_end()]

        return "\n".join(lines)

    def flush(self) -> None:
        worker_info = get_worker_info()
        if worker_info.worker_id == 0 and self.total_exceptions > 0:
            logger.info("Exception summary:\n\n%s\n", self.summary())
        self.exceptions.clear()
        self.exception_classes.clear()
        self.exception_locs.clear()
        self.steps = 0
        self.total_exceptions = 0


class ErrorHandlingDataset(Dataset[BatchT]):
    """Defines a wrapper for safely handling errors."""

    def __init__(self, dataset: Dataset[BatchT], config: ErrorHandlingConfig) -> None:
        super().__init__()

        self.dataset = dataset
        self.config = config
        self.exc_summary = ExceptionSummary(config)

    def __getitem__(self, index: int) -> BatchT:
        num_exceptions = 0
        backoff_time = self.config.sleep_backoff
        self.exc_summary.step()
        while num_exceptions < self.config.maximum_exceptions:
            try:
                return self.dataset[index]
            except bdb.BdbQuit as e:
                logger.info("User interrupted debugging session; aborting")
                raise e
            except Exception as e:
                if self.config.log_full_exception:
                    logger.exception("Caught exception on index %d", index)
                self.exc_summary.add_exception(e, get_loc(self.config.exception_location_traceback_depth))
                index = random.randint(0, len(self) - 1)
            num_exceptions += 1
            if num_exceptions > self.config.backoff_after:
                logger.error(
                    "Encountered %d exceptions for a single index, backing off for %f seconds",
                    num_exceptions,
                    backoff_time,
                )
                time.sleep(backoff_time)
                backoff_time *= self.config.sleep_backoff_power
        exc_message = f"Reached max exceptions {self.config.maximum_exceptions}\n{self.exc_summary.summary()}"
        if self.exc_summary.last_exception is None:
            raise RuntimeError(exc_message)
        raise RuntimeError(exc_message) from self.exc_summary.last_exception

    def __len__(self) -> int:
        if hasattr(self.dataset, "__len__"):
            return self.dataset.__len__()
        raise NotImplementedError("Base dataset doesn't implemenet `__len__`")


@functional_datapipe("map_error_handling")
class ErrorHandlingMapDataPipe(ErrorHandlingDataset[BatchT], MapDataPipe[BatchT]):
    """Defines a wrapper for safely handling errors."""

    def __init__(self, datapipe: MapDataPipe[BatchT], config: ErrorHandlingConfig) -> None:
        ErrorHandlingDataset.__init__(self, datapipe, config)
        MapDataPipe.__init__(self)


class ErrorHandlingIterableDataset(IterableDataset[BatchT]):
    """Defines a wrapper for safely handling errors in iterable datasets."""

    def __init__(self, dataset: IterableDataset[BatchT], config: ErrorHandlingConfig) -> None:
        super().__init__()

        self.iteration = 0
        self.dataset = dataset
        self.config = config
        self.exc_summary = ExceptionSummary(config)
        self.iter: Iterator[BatchT] | None = None

        self._configured_logging = False

    def __iter__(self) -> Iterator[BatchT]:
        self.iter = self.dataset.__iter__()
        self.iteration = 0
        return self

    def __next__(self) -> BatchT:
        assert self.iter is not None, "Must call `__iter__` before `__next__`"
        num_exceptions = 0
        backoff_time = self.config.sleep_backoff
        self.exc_summary.step()
        self.iteration += 1
        while num_exceptions < self.config.maximum_exceptions:
            try:
                return self.iter.__next__()
            except bdb.BdbQuit as e:
                logger.info("User interrupted debugging session; aborting")
                raise e
            except StopIteration as e:
                raise e
            except Exception as e:
                if self.config.log_full_exception:
                    logger.exception("Caught exception on iteration %d", self.iteration)
                self.exc_summary.add_exception(e, get_loc(self.config.exception_location_traceback_depth))
            num_exceptions += 1
            if num_exceptions > self.config.backoff_after:
                logger.error(
                    "Encountered %d exceptions for a single index, backing off for %f seconds",
                    num_exceptions,
                    backoff_time,
                )
                time.sleep(backoff_time)
                backoff_time *= self.config.sleep_backoff_power
        raise RuntimeError(f"Reached max exceptions {self.config.maximum_exceptions}\n{self.exc_summary.summary()}")


@functional_datapipe("iter_error_handling")
class ErrorHandlingIterDataPipe(ErrorHandlingIterableDataset[BatchT], IterDataPipe[BatchT]):
    """Defines a wrapper for safely handling errors in iterable datapipe."""

    def __init__(self, datapipe: IterDataPipe[BatchT], config: ErrorHandlingConfig) -> None:
        ErrorHandlingIterableDataset.__init__(self, datapipe, config)
        IterDataPipe.__init__(self)


@no_type_check
def error_handling_dataset(dataset: DatasetT, config: ErrorHandlingConfig) -> DatasetT:
    """Returns a dataset which wraps the base dataset and handles errors.

    Args:
        dataset: The dataset to handle errors for
        config: An associated config, describing which errors to handle

    Returns:
        The wrapped dataset, which catches some errors

    Raises:
        NotImplementedError: If the dataset type is not supported
    """
    if isinstance(dataset, MapDataPipe):
        return ErrorHandlingMapDataPipe(dataset, config)
    if isinstance(dataset, IterDataPipe):
        return ErrorHandlingIterDataPipe(dataset, config)
    if isinstance(dataset, IterableDataset):
        return ErrorHandlingIterableDataset(dataset, config)
    elif isinstance(dataset, Dataset):
        return ErrorHandlingDataset(dataset, config)
    raise NotImplementedError(f"Unexpected type: {dataset}")


def test_exception_summary() -> None:
    summary = ExceptionSummary(ErrorHandlingConfig())
    for i in range(10):
        try:
            if i < 7:
                raise RuntimeError("test")
            else:
                raise ValueError("test 2")
        except Exception as e:
            summary.add_exception(e, get_loc())
        summary.step()
    print(summary.summary())


if __name__ == "__main__":
    # python -m ml.tasks.datasets.error_handling
    test_exception_summary()
