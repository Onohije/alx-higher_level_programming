#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: When called on the base class.
        """
        raise Exception("area() is not implemented")
