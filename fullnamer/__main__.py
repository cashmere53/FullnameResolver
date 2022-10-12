# -*- coding: utf-8 -*-

import sys
from os import fspath

import loguru
from loguru import logger

from fullnamer.commandline import parse_input
from fullnamer.fullnamer import resolve_filepath


def main() -> None:
    commandline_info = parse_input()

    logger.remove()
    logging_level: str = "SUCCESS"
    if commandline_info.verbose == 1:
        logging_level = "INFO"
    elif commandline_info.verbose == 2:
        logging_level = "DEBUG"
    elif commandline_info.verbose >= 3:
        logging_level = "TRACE"
    logger.add(sys.stdout, level=logging_level)

    logger.debug(f"{commandline_info}")
    resolve_path = resolve_filepath(commandline_info.path, check_exists=commandline_info.exist)

    for item in resolve_path:
        print(fspath(item))


if __name__ == "__main__":
    main()
