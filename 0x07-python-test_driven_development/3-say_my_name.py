#!/usr/bin/python3
"""
This is the say_my_name_0987c module.

This module supplies one function, say_my_name_0987c().
"""


def say_my_name_0987c(first_name, last_name=""):
    """
    Print My name is <first name> <last name>.

    Args:
        first_name (str): the first name.
        last_name (str): the last name.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
