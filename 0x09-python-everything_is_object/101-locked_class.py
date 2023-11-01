#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except for the attribute 'first_name'.
    """

    __slots__ = ["first_name"]
