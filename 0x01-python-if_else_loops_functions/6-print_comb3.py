#!/usr/bin/python3
# printing possible combination of 2 digit numbers in ascending order.
# The digits are to be different and 10 and 01 are to considered identical.

for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print(f"{digit1}{digit2}")
        else:
            print(f"{digit1}{digit2}", end=", ")
