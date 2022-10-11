# -*- coding: utf-8 -*-

from pathlib import Path

PathStr = Path | str


def resolve_filepath(path: PathStr) -> Path:
    inner_path: Path | None = None
    if isinstance(path, str):
        inner_path = Path(path)
    elif isinstance(path, Path):
        inner_path = path
    else:
        raise ValueError()

    if inner_path is None:
        raise ValueError()

    if not inner_path.exists():
        raise FileNotFoundError()

    return inner_path.resolve()
