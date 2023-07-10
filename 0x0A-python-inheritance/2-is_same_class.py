#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.
    Returns:
        True if obj is an instance of target_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
