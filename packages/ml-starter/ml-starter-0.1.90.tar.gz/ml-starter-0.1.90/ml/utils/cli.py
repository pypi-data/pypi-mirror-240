"""Command-line interface utilities."""

import logging
import sys
from functools import partial
from pathlib import Path
from typing import cast

from omegaconf import DictConfig, OmegaConf

from ml.core.env import get_default_config_root_path, get_global_tags, set_exp_name, set_ml_config_path

logger: logging.Logger = logging.getLogger(__name__)


IGNORE_ARGS: set[str] = {
    "trainer.exp_name",
    "trainer.log_dir_name",
    "trainer.exp_dir",
    "trainer.name",
}


def get_exp_name(prefix: str | None = None, args: list[str] | None = None) -> str:
    parts: list[str] = []
    if prefix is not None:
        parts += [prefix]
    if args is not None:
        parts += args
    if not parts:
        parts = ["run"]
    parts += get_global_tags()
    return ".".join(p for p in parts if p)


def get_stem(path_str: str) -> str:
    path = Path(path_str).resolve()

    # Remove the `.yaml` suffix.
    path = path.parent / path.stem

    # Special handling for paths that are relative to the configs directory.
    for parent in path.parents:
        if parent.stem in ("conf", "config", "configs"):
            return ".".join(path.relative_to(parent).parts)

    return path.stem


def get_default_configs() -> list[Path]:
    root_dir = get_default_config_root_path()
    if not root_dir.is_dir():
        return []
    return sorted(root_dir.glob("*.yaml"))


def parse_cli(args: list[str]) -> DictConfig:
    """Parses the remaining command-line arguments to a raw config.

    Args:
        args: The raw command-line arguments to parse

    Returns:
        The raw config, loaded from the provided arguments
    """

    def show_help() -> None:
        print("\nUsage: cmd <path/to/config.yaml> [<new_config.yaml>, ...] overrida.a=1 override.b=2", file=sys.stderr)
        sys.exit(1)

    if len(args) == 0 or "-h" in args or "--help" in args:
        show_help()

    # Builds the configs from the command-line arguments.
    config = DictConfig({})
    argument_parts: list[str] = []
    paths: list[Path] = []

    # Parses all of the config paths.
    while len(args) > 0 and (args[0].endswith(".yaml") or args[0].endswith(".yml")):
        paths, new_stem, args = paths + [Path(args[0])], get_stem(args[0]), args[1:]
        argument_parts.append(new_stem)

    # Parses all of the additional config overrides.
    if len(args) > 0:
        split_args = [a.split("=") for a in args]
        assert all(len(a) == 2 for a in split_args), f"Got invalid arguments: {[a for a in split_args if len(a) != 2]}"
        argument_parts += [f"{k.split('.')[-1]}_{v}" for k, v in sorted(split_args) if k not in IGNORE_ARGS]

    # Registers an OmegaConf resolver with the job name.
    OmegaConf.register_new_resolver("ml.exp_name", partial(get_exp_name, args=argument_parts), replace=True)
    set_exp_name(get_exp_name(args=argument_parts))

    # Special handling if there is exactly one path.
    if len(paths) == 1 and paths[0].name == "config.yaml":
        set_ml_config_path(paths[0])

    # Adds any default configs.
    paths = get_default_configs() + paths

    # Finally, builds the config.
    try:
        for path in paths:
            config = cast(DictConfig, OmegaConf.merge(config, OmegaConf.load(path)))
        config = cast(DictConfig, OmegaConf.merge(config, OmegaConf.from_dotlist(args)))
    except Exception:
        logger.exception("Error while creating dotlist")
        show_help()

    return config
