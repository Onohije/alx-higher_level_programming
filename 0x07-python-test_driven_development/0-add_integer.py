#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function for performing integer addition."""


def add_integer(a, b=98):
    """Returns the addition of two numbers, a and b.

    Float arguments are typecasted to integers before the addition operation.

    Raises:
        TypeError: If either of the arguments is not an integer nor a float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
