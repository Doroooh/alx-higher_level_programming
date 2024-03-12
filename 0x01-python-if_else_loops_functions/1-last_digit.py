#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
my_lastdigit = abs(number) % 10
if number < 0:
    my_lastdigit = -my_lastdigit

print(f"Last digit of {number} is {my_lastdigit} and is ", end="")
if my_lastdigit > 5:
    print("greater than 5")
elif my_lastdigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
