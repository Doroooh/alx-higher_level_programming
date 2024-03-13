#!/usr/bin/python3
# printing possible combination of 2 digit numbers in ascending order.
# The digits are to be different and 10 and 01 are to considered identical.

for number_digit_one in range(0, 10):
    for number_digit_two in range(number_digit_one + 1, 10):
        if number_digit_one == 8 and number_digit_two == 9:
            print("{}{}".format(number_digit_one, number_digit_two))
        else:
            print("{}{}".format(number_digit_one, number_digit_two), end=", ")
