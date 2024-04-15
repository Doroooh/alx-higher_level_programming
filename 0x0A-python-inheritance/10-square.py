#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry

"""


class Square(Rectangle):
    """Square class  will inherit from the  Rectangle that inherits the BaseGeometry"""

    def __init__(self, size):
        """initialized attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
