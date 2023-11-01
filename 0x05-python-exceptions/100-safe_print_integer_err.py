#!/usr/bin/python3

def safe_print_integer_err(value):

    """
    Prints an integer using "{:d}".format().

    If a ValueError is caught,
    a corresponding message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is successfully printed,
        False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except TypeError:
        return False
    except ValueError as e:
        import sys
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
