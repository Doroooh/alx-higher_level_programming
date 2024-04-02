#!/usr/bin/python3
"""Square generation  module.

The class that defines a square and init method that
sets its size.

"""

class Square():
    """Defining a square."""

    def __init__(self, size):
        """Setting necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
