#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Last_dig = number % -10
else:
    Last_dig = number % 10
if Last_dig > 5:
    print(f"Last digit of {number} is {Last_dig} and is greater than 5")
if Last_dig == 0:
    print(f"Last digit of {number} is {Last_dig} and is 0")
elif number < 6 and number != 0:
    print(f"Last digit of {number} is {Last_dig} and is less than 6 and not 0")
