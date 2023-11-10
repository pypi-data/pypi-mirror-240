import argparse
import os
from typing import Any


def is_valid_file(parser: argparse.ArgumentParser, arg: Any):
    """Check if the value points to a valid file

    Parameters
    ----------
    parser : argparse.ArgumentParser
        The ArgumentParser object
    arg : Any
        Value of the option

    Returns
    -------
    arg : str
        Option's value if it points to a valid file
    Examples
    --------
    For CLI options that should be pointing to files

    >>> test_parser = argparse.ArgumentParser()
    >>> test_parser.add_argument("input_file", type=lambda x: is_valid_file(test_parser, x))
    >>> args = test_parser.parse_args(["a_non_existing_file"])
    """
    if not os.path.isfile(arg):
        parser.error('The file {} does not exist!'.format(arg))
    else:
        # File exists so return the filename
        return arg
