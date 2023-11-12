"""Logging utilities.

This extends the basic Python logger to log across all ranks, and to colorize
the logs to make them easier to parse.
"""

import logging
import math
import sys
import time

from ml.core.env import is_debugging, should_show_all_logs
from ml.utils.colors import Color, colorize, get_colorize_parts

# Logging level to show on all ranks.
INFOALL: int = logging.INFO + 1
DEBUGALL: int = logging.DEBUG + 1


class RankFilter(logging.Filter):
    def __init__(self, *, rank: int | None = None) -> None:
        """Logging filter which filters out INFO logs on non-zero ranks.

        Args:
            rank: The current rank
        """
        super().__init__()

        self.rank = rank

        # Log using INFOALL to show on all ranks.
        logging.addLevelName(INFOALL, "INFOALL")
        logging.addLevelName(DEBUGALL, "DEBUGALL")
        levels_to_log_all_ranks = (DEBUGALL, INFOALL, logging.CRITICAL, logging.ERROR, logging.WARNING)
        self.log_all_ranks = {logging.getLevelName(level) for level in levels_to_log_all_ranks}

    def filter(self, record: logging.LogRecord) -> bool:
        if self.rank is None or self.rank == 0:
            return True
        if record.levelname in self.log_all_ranks:
            return True
        return False


class ColoredFormatter(logging.Formatter):
    """Defines a custom formatter for displaying logs."""

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"

    COLORS: dict[str, Color] = {
        "WARNING": "yellow",
        "INFOALL": "magenta",
        "INFO": "cyan",
        "DEBUGALL": "grey",
        "DEBUG": "grey",
        "CRITICAL": "yellow",
        "FATAL": "red",
        "ERROR": "red",
    }

    def __init__(
        self,
        *,
        prefix: str | None = None,
        rank: int | None = None,
        world_size: int | None = None,
        use_color: bool = True,
    ) -> None:
        asc_start, asc_end = get_colorize_parts("grey")
        message = "{levelname:^19s} " + asc_start + "{asctime}" + asc_end + " [{name}] {message}"
        if prefix is not None:
            message = colorize(prefix, "white") + " " + message
        if rank is not None or world_size is not None:
            assert rank is not None and world_size is not None
            digits = int(math.log10(world_size) + 1)
            message = "[" + colorize(f"{rank:>{digits}}", "blue", bold=True) + "] " + message
        super().__init__(message, style="{", datefmt="%Y-%m-%d %H:%M:%S")

        self.rank = rank
        self.use_color = use_color

    def format(self, record: logging.LogRecord) -> str:
        levelname = record.levelname

        match levelname:
            case "DEBUG":
                record.levelname = ""
            case "INFOALL":
                record.levelname = "INFO"
            case "DEBUGALL":
                record.levelname = "DEBUG"

        if record.levelname and self.use_color and levelname in self.COLORS:
            record.levelname = colorize(record.levelname, self.COLORS[levelname], bold=True)
        return logging.Formatter.format(self, record)


class TqdmHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        import tqdm

        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg)
            self.flush()
        except Exception:
            self.handleError(record)


def configure_logging(
    *,
    prefix: str | None = None,
    rank: int | None = None,
    world_size: int | None = None,
    use_tqdm: bool = True,
) -> None:
    """Instantiates print logging, to either stdout or tqdm.

    Args:
        prefix: An optional prefix to add to the logger
        rank: The current rank, or None if not using multiprocessing
        world_size: The total world size, or None if not using multiprocessing
        use_tqdm: Write using TQDM instead of sys.stdout
    """
    if rank is not None or world_size is not None:
        assert rank is not None and world_size is not None
    root_logger = logging.getLogger()
    while root_logger.hasHandlers():
        root_logger.removeHandler(root_logger.handlers[0])

    try:
        import tqdm  # noqa: F401
    except ImportError:
        use_tqdm = False

    handler = TqdmHandler() if use_tqdm else logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter(prefix=prefix, rank=rank, world_size=world_size))
    handler.addFilter(RankFilter(rank=rank))
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG if is_debugging() else logging.INFO)

    # Avoid junk logs from other libraries.
    if not should_show_all_logs():
        logging.getLogger("matplotlib").setLevel(logging.WARNING)
        logging.getLogger("PIL").setLevel(logging.WARNING)
        logging.getLogger("torch").setLevel(logging.WARNING)


class IntervalTicker:
    def __init__(self, interval: float) -> None:
        self.interval = interval
        self.last_tick_time: float | None = None

    def tick(self) -> bool:
        tick_time = time.time()
        if self.last_tick_time is None or tick_time - self.last_tick_time > self.interval:
            self.last_tick_time = tick_time
            return True
        return False
