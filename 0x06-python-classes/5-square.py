#!/usr/bin/python3
"""Square generation
"""


class Square:
    """the class defined for square generation.

    Args:
        size (int): length of one side of the square

    Attributes:
        __size (int): the length of one side of the square

    """

    def __init__(self, size=0):
        # the attribute assigment engages the setters defined
        self.size = size

    @property
    def size(self):
        """__size getter,the setter with same method name

        Returns:
            __size (int): the length of one side, squared

        """
        return self.__size

    @size.setter
    def size(self, value1):
        """Args:
            value1 (int):the length of one side of the square

        Attributes:
            __size (int): the length of one side of the square

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0

        """
        if type(value1) is not int:
            raise TypeError('the size must be an integer')
        if value1 < 0:
            raise ValueError('the size must be >= 0')
        self.__size = value1

    def area(self):
        """This calulates the area of the square.

        Attributes:
            __size (int): length of one side of the square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Printing the text representation of the square in hash chars.

        Attributes:
            __size (int): the length of one side of square

        """
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
