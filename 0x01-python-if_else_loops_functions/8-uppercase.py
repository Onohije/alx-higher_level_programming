#!/usr/bin/python3
def uppercase(str):
    for char in str:
        a = ord(char)
        if a in range(97, 123):
            up_char = 32
        else:
            up_char = 0
        print("{:c}".format(a - up_char), end="")
    print()
