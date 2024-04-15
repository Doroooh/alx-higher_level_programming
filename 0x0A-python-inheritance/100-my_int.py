#!/usr/bin/python3
"""
Module with a class MyInt
"""


class MyInt(int):
    """Class that will inherit from int"""

    def __init__(self, my_int):
        """Initialize a value my_int"""
        super().__init__(my_int)

    def __eq__(self, other):
        """Override equality operator"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override  inequality operator"""
        return not super().__ne__(other)
