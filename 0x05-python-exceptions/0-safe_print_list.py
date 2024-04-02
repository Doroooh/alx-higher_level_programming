#!/usr/bin/python3

def safe_print_list(my_lst=None, x=0):
    """
    Printing the first 'x' elements of a list.

    Args:
        my_lst (list): List to print elements from.
        x (int): Number of elements to print.

    Returns:
        int: Number of elements actually printed.
    """
    if my_lst is None:
        my_lst = []

    try:
        count = 0
        for elemt in my_lst[:x]:
            print("{} ".format(elemt), end="")
            count += 1
        print()  # Adding a newline after printing the element.
        return count
    except Exception as e:
        print("Exception: {}".format(e))
        return 0
