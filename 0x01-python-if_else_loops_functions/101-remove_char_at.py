#!/usr/bin/python3
# creating the string copy without character that is in position n
def remove_char_at(string, n):
    if 0 > n:
        return string
    return string[:n] + string[n+1:]
