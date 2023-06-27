#!/usr/bin/python3
"""
    This class represents a square.

    It provides methods and attributes for working with square shapes.
    """


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """
        Validate the size value and ensure it is a positive integer.

        Args:
            value: The value to validate.

        Returns:
            int: The validated size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
