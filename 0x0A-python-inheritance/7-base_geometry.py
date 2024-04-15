#!/usr/bin/python3
"""
Module with a unique BaseGeometry

"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Calculate area method"""
        raise NotImplementedError("Area calculation not implemented")

    def validate_integer(self, name, value):
        """Validate if the value is an integer that is greater than zero"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
