#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """
    Divide two lists element by element up to a specified length.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing
        the results of element-wise division.
    """
    result_list = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result_list.append(quotient)
    return (result_list)
