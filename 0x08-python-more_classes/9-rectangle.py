#!/usr/bin/python3
"""Defines a Rectangle class with various methods and properties."""

class Rectangle:
    """Represents a rectangle with width and height properties."""

    # Class attribute to keep track of the number of instances created
    number_of_instances = 0

    # Class attribute to define the default print symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the areas of two rectangles and returns the bigger one.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the bigger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new rectangle instance that is a square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new rectangle instance that is a square.
        """
        return cls(size, size)

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using the print symbol.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            row = []
            for j in range(self.__width):
                row.append(self.print_symbol)
            rectangle.append("".join(row))
        return "\n".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used to recreate the instance.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
