#!/usr/bin/env python3

def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []
    count = 0

    for index in range(x):
        try:
            print(my_list[index], end='')
            count += 1
        except IndexError:
            # Break out of the loop if we try to access beyond the list's length
            break

    # Ensuring the output starts on a new line after the list elements are printed
    print()

    return count
