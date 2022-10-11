# -*- coding: utf-8 -*-

from pathlib import Path
from re import Match, fullmatch
from typing import Optional

from template import __version__


def test_version() -> None:
    pyproject_file: Path = Path("./pyproject.toml")
    with pyproject_file.open("r") as fp:
        buffer: str = list(filter(lambda x: x.startswith("version"), fp))[0]
    m_res: Optional[Match[str]] = fullmatch(r'version = "(.*)"\n', buffer)
    if m_res is None:
        raise ValueError("version string is not found in pyproject.toml")
    version: str = m_res[1]

    assert __version__ == version
