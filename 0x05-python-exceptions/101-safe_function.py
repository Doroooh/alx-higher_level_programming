#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Safely calings a function with the arguments that are provided.

    Args:
        fct (function): The function to call.
        *args: the variable number of arguments to pass to the function.

    Returns:
        Any: Result of the function call, or None if an exception occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
