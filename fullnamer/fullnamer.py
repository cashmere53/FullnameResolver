# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Sequence

from loguru import logger

PathStr = Path | str


def resolve_filepath(path: Sequence[PathStr], check_exists: bool = False) -> list[Path]:
    return_list: list[Path] = []
    for item in path:
        return_list.append(resolve_single(item, check_exists))

    return return_list


def resolve_single(path: PathStr, check_exists: bool) -> Path:
    inner_path: Path | None = None
    if isinstance(path, str):
        inner_path = Path(path)
    elif isinstance(path, Path):
        inner_path = path
    else:
        raise ValueError(f"invalid input type: [{type(path)}]{path}")

    resolved_path: Path = inner_path.resolve()

    logger.debug(f"{check_exists=}, {resolved_path.exists()=}")
    if check_exists and not resolved_path.exists():
        raise FileNotFoundError(f"input file is not found. {resolved_path}")

    return resolved_path
