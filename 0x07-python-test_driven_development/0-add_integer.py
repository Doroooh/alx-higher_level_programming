#!/usr/bin/python3

def add_integer(a, b=98):
    """
    A function that adds 2 integers.

    If both a and b are not integers or floats, raise a TypeError exception
    with the message 'a must be an integer or b must be an integer'

    a and b should be casted to integers if they are float

    Returns an integer: the addition of a and b

    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
