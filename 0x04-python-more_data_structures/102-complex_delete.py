#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    list_keys = [key for key, val in a_dictionary.items() if val == value]
    for value_dic in list_keys:
        del a_dictionary[value_dic]

    return (a_dictionary)
