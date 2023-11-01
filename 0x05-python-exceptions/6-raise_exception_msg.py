#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raise a NameError exception with an optional message.

    Args:
        message (str, optional): The error message to be
        associated with the exception.

    Raises:
        NameError: This exception is raised intentionally
        with the specified message.
    """
    raise NameError(message)
