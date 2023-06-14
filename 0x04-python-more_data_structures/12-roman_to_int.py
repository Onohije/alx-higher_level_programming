#!/usr/bin/python3

def to_subtract(list_num):
    subt = 0
    max_list = max(list_num)

    for num in list_num:
        if max_list > num:
            subt += num

    return (max_list - subt)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_dict.keys())

    numb = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if r_dict.get(ch) <= last_rom:
                    numb += to_subtract(list_num)
                    list_num = [r_dict.get(ch)]
                else:
                    list_num.append(r_dict.get(ch))

                last_rom = r_dict.get(ch)

    numb += to_subtract(list_num)

    return (numb)
