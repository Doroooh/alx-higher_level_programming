#!/usr/bin/python3

""" 
Empty class Rectangle that defines a rectangle
"""

class Rectangle:
    """ 
    Class representing a rectangle.
    """

    def __init__(self, width=0, height=0):
        """ 
        Initializes a rectangle with a width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ 
        Getter method for width.
        """
        return self.__width

    @property
    def height(self):
        """ 
        Getter method for height.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ 
        Setter method for width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ 
        Setter method for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
