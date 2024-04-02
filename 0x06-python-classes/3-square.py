#!/usr/bin/python3


class Square:
    """Class defined for the square generation.

    Args:
        size (int): the length of one side of the square

    Attributes:
        __size (int): the length of one side of a square

    Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0

    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('the size must be an integer')
        if size < 0:
            raise ValueError('the size must be >= 0')
        self.__size = size

    def area(self):
        """Calulating the area of a square.

        Attributes:
            __size (int): the length of one side of the square

        Returns:
            area (int): the length of one side, squared

        """
        area = self.__size * self.__size
        return area
