#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct (callable): The function to execute.
        *args: Arguments to be passed to the function.

    Returns:
        None: If an error occurs during execution.
        Any: The result of the function call if successful.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
