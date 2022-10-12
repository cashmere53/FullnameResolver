# -*- coding: utf-8 -*-

import sys
from os import fspath

from loguru import logger

from fullnamer.commandline import parse_input
from fullnamer.fullnamer import resolve_filepath


def main() -> None:
    commandline_info = parse_input()
    setup_logger(commandline_info.verbose)

    logger.debug(f"{commandline_info}")
    resolve_path = resolve_filepath(commandline_info.path, check_exists=commandline_info.exist)

    for item in resolve_path:
        print(fspath(item))


def setup_logger(verbosity: int = 0) -> None:
    logger.remove()

    logging_level: str = "SUCCESS"
    if verbosity == 1:
        logging_level = "INFO"
    elif verbosity == 2:
        logging_level = "DEBUG"
    elif verbosity >= 3:
        logging_level = "TRACE"

    logger.add(sys.stderr, level=logging_level)


if __name__ == "__main__":
    main()
