#!/usr/bin/python3

def magic_calculation(a, b):
    """
    Perform a magic calculation using the provided parameters.

    Args:
        a (int): The first parameter.
        b (int): The second parameter.

    Returns:
        float or int: The result of the magic calculation.

    Raises:
        Exception: Raised with the message 'Too far'
          if i is greater than a during the calculation.
    """
    result_cal = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result_cal += a ** b / i
        except:
            result_cal = b + a
            break
    return (result_cal)
