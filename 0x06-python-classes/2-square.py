#!/usr/bin/python3

class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """
        initialization function for the square class
        checks for input errors for size
        """
        if type(size) != int:
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("the size must be >= 0")
        else:
            self.__size = size
