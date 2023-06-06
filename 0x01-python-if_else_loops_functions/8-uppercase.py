#!/usr/bin/python3
def uppercase(str):
    for char in str:
        a = ord(char)
        if a in range(97, 122):
            up_char = chr(a - 32)
        else:
            uppercase_char = char
        print(up_char, end='')
    print()
