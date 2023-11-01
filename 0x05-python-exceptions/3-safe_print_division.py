#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divide two numbers and handle potential errors.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or None: The division result if successful;
        None if a TypeError or ZeroDivisionError occurs.
    """

    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
