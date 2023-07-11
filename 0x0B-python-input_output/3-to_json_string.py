#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object.

    Args:
        my_obj: The Python object to convert to JSON.

    Returns:
        str: A string representing the JSON-encoded object.
    """
    return json.dumps(my_obj)
