#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        obj: The Python object representation of the JSON string.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
