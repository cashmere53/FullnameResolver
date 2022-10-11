# -*- coding: utf-8 -*-

from os import fspath

from fullnamer.fullnamer import resolve_filepath


def main() -> None:
    import sys

    resolve_path = resolve_filepath(sys.argv[1])
    print(fspath(resolve_path))


if __name__ == "__main__":
    main()
