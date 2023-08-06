"""
Python package template with command-line interface
"""

from . import __version__
import argparse


def cli_args():
    """Define & examine command-line arguments & options."""
    p = argparse.ArgumentParser(
        prog=__package__,
        description=__doc__.strip().splitlines()[0],
        epilog=f"{__package__} is for demonstration.",
    )
    p.add_argument("-v", "--version", action="version", version=__version__)
    return p.parse_args()


def main():
    args = cli_args()
    # simple function of this package, return a string
    s = f"{__name__} version {__version__} of '{__file__}', args={args}"
    return s


if __name__ == "__main__":
    main()
