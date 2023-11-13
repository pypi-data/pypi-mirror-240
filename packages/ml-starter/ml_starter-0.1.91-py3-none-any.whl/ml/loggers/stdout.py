"""Defines a simple logger that writes to stdout.

I put a bunch of colors in here to make it easier to quickly find logged
values of interest, but the colors can be disabled by setting the
environment variable ``DISABLE_COLORS=1``
"""

import datetime
import itertools
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from torch import Tensor

from ml.core.config import conf_field
from ml.core.registry import register_logger
from ml.core.state import Phase, State
from ml.loggers.base import BaseLogger, BaseLoggerConfig
from ml.utils.colors import Color, colorize
from ml.utils.datetime import format_timedelta
from ml.utils.distributed import is_distributed

LEVEL_COLORS: list[Color] = ["light-cyan", "cyan"]


@dataclass
class StdoutLoggerConfig(BaseLoggerConfig):
    precision: int = conf_field(4, help="Scalar precision to log")


def format_number(value: int | float, precision: int) -> str:
    if isinstance(value, int):
        return str(value)
    return f"{value:.{precision}g}"


def as_str(value: Any, precision: int) -> str:  # noqa: ANN401
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, Tensor):
        value = value.detach().float().cpu().item()
    if isinstance(value, (int, float)):
        return format_number(value, precision)
    raise TypeError(f"Unexpected log type: {type(value)}")


@register_logger("stdout", StdoutLoggerConfig)
class StdoutLogger(BaseLogger[StdoutLoggerConfig]):
    def __init__(self, config: StdoutLoggerConfig) -> None:
        super().__init__(config)

        self.log_values: dict[Phase, dict[str, dict[str, Callable[[], Any]]]] = {}
        self.logger = logging.getLogger("stdout")

    def initialize(self, log_directory: Path) -> None:
        super().initialize(log_directory)

        log_directory.mkdir(exist_ok=True, parents=True)
        file_handler = logging.FileHandler(log_directory / "stdout.log")
        self.logger.addHandler(file_handler)
        self.logger.debug("Finished initializing logger")

    def get_log_dict(self, state: State, namespace: str | None) -> dict[str, Callable[[], Any]]:
        if namespace is None:
            namespace = "default"
        if state.phase not in self.log_values:
            self.log_values[state.phase] = {}
        if namespace not in self.log_values[state.phase]:
            self.log_values[state.phase][namespace] = {}
        return self.log_values[state.phase][namespace]

    def log_scalar(self, key: str, value: Callable[[], int | float | Tensor], state: State, namespace: str) -> None:
        self.get_log_dict(state, namespace)[key] = value

    def log_string(self, key: str, value: Callable[[], str], state: State, namespace: str) -> None:
        self.get_log_dict(state, namespace)[key] = value

    def write(self, state: State) -> None:
        if not (phase_log_values := self.log_values.get(state.phase)):
            return

        # Gets elapsed time since last write.
        elapsed_time = datetime.timedelta(seconds=state.elapsed_time_s)
        elapsed_time_str = format_timedelta(elapsed_time)

        def get_section_string(name: str, section: dict[str, Any], level: int = 0) -> str:
            sub_sections: dict[str, dict[str, Any]] = {}
            section_keys = list(section.keys())
            for k in section_keys:
                ks = k.split("/", maxsplit=1)
                if len(ks) == 2:
                    kk, rest = ks
                    if kk not in sub_sections:
                        sub_sections[kk] = {}
                    sub_sections[kk][rest] = section[k]
                    section.pop(k)

            def get_line(kv: tuple[str, Any]) -> str:
                return f'"{kv[0]}": {as_str(kv[1](), self.config.precision)}'

            inner_str = ", ".join(
                itertools.chain(
                    map(get_line, sorted(section.items())),
                    (get_section_string(k, v, level + 1) for k, v in sorted(sub_sections.items())),
                )
            )
            level_color = LEVEL_COLORS[min(level, len(LEVEL_COLORS) - 1)]
            return '"' + colorize(name, level_color) + '": {' + inner_str + "}"

        def colorize_phase(phase: Phase) -> str:
            match phase:
                case "train":
                    return colorize(phase, "green", bold=True)
                case "valid":
                    return colorize(phase, "yellow", bold=True)
                case "test":
                    return colorize(phase, "red", bold=True)
                case _:
                    return colorize(phase, "white", bold=True)

        def colorize_time(time: str) -> str:
            return colorize(time, "light-magenta")

        # Writes a log string to stdout.
        log_string = ", ".join(get_section_string(k, v) for k, v in sorted(phase_log_values.items()))
        self.logger.info("%s [%s] {%s}", colorize_phase(state.phase), colorize_time(elapsed_time_str), log_string)

        # Clears the log values.
        phase_log_values.clear()

    def default_write_every_n_seconds(self, state: State) -> float:
        return 10.0 if is_distributed() or state.num_steps > 5000 else 1.0
