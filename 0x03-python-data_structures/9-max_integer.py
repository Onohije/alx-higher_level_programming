#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    maximum = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > maximum:
            maximum = my_list[num]

    return (maximum)
