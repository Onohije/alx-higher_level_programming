#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5

    result = add(a, b)
    result1 = sub(a, b)
    result2 = div(a, b)
    result3 = mul(a, b)

    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, result1))
    print("{} / {} = {}".format(a, b, result2))
    print("{} * {} = {}".format(a, b, result3))
