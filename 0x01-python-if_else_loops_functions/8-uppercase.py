#!/usr/bin/python3
# printing uppercase letters that is capital letters
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
