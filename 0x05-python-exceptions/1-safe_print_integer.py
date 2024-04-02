#!/usr/bin/python3

def safe_print_integer(myValue):
    """
    Safely prints integer values.

    Args:
        myValue (int): Integer value for printing.

    Returns:
        bool: if printing is successful True, False otherwise.
    """
    try:
        print("{:d}".format(myValue))
        return True
    except (ValueError, TypeError):
        return False
