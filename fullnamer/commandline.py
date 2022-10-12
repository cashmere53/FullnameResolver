# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from dataclasses import dataclass, field

from fullnamer.__init__ import __version__


@dataclass
class CommandLineInput:
    path: list[str] = field(default_factory=list)
    clip: bool = False
    exist: bool = False
    verbose: int = 0


def setup_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("path", help="resolve path", nargs="+")
    parser.add_argument("-c", "--clip", help="copy resolve path to clipboard", action="store_true")
    parser.add_argument("-e", "--exist", help="check input path to exist", action="store_true")
    parser.add_argument("-v", "--verbose", help="output log verbosity", action="count")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    return parser


def parse_input() -> CommandLineInput:
    input_params: CommandLineInput = CommandLineInput()
    setup_parser().parse_args(namespace=input_params)

    return input_params
