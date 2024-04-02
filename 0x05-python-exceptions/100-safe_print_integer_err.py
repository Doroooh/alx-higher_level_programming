#!/usr/bin/python3
import sys

def safe_print_integer_err(value1):
    """
    This safely prints the integer value and prints exception to stderr.

    Args:
        value1 (int): integer value to print.

    Returns:
        bool: True if the printing is successful, False otherwise.
    """

    try:
        print("{:d}".format(value1))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
