from argparse import ArgumentParser
from zut import add_module_command
from .bases import BaseContext, main_base
from .commands import report


def main():
    main_base(BaseContext)


def add_arguments(parser: ArgumentParser):
    subparsers = parser.add_subparsers(title="commands")
    add_module_command(subparsers, report)


if __name__ == '__main__':
    main()
