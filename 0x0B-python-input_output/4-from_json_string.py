#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""

import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        obj: The Python object representation of the JSON string.
    """
    return json.loads(my_str)
