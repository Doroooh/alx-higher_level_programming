#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints the first 'x' elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements actually printed.

    """
    try:
        count = 0
        for elem in my_list:
            if count < x:
                print("{} ".format(elem), end="")
                count += 1
            else:
                break
        print("")  # Add a newline after printing elements.
        return count
    except Exception as e:
        print("Exception: {}".format(e))
        return 0
