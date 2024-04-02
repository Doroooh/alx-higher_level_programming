#!/usr/bin/python3

class Square():
    """Defining a square."""

    def __init__(self, size=0):
        """Setting necessary attributes for Square object.

        Args:
            size (int): size of one edge of the square.

        Raises:
            TypeError: if the size is not given as an integer.
            ValueError: if the size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("the size must be >= 0")
        else:
            raise TypeError("the size must be an integer")
