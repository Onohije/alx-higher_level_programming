#!/usr/bin/python3
"""Defines a function to retrieve a list of object attributes."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
