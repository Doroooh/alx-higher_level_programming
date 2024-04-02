#!/usr/bin/python3

#!/usr/bin/python3

class CustomSquare:
    """A class for representing a square with a specified size."""
    def __init__(self, size=0):
        """Initialize a square object with a given size."""
        if not isinstance(size, int):
            raise TypeError('Size must be an integer')
        if size < 0:
            raise ValueError('Size must be non-negative')
        self.__size = size
