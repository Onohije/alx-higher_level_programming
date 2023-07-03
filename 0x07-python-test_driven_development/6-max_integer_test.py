#!/usr/bin/python3
"""Module to find the maximum integer in a list.
"""


def max_integer(list=[]):
    """Function to find the maximum integer in a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int: The maximum integer found in the list.
    """
    if len(list) == 0:
        return None
    max_number = list[0]
    num = 1
    while num < len(list):
        if list[num] > max_number:
            max_number = list[num]
        num += 1
    return (max_number)
