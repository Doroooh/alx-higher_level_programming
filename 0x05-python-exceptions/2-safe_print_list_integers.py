#!/usr/bin/python3

def safe_print_list_integers(my_lst=None, x=0):
    """
    Safely printing the first 'x' integers from a list.

    Args:
        my_lst (list): The list to print integers from.
        x (int): The number of integers to print.

    Returns:
        int: The number of integers actually printed.
    """
    if my_lst is None:
        my_lst = []
    
    count = 0

    try:
        for item in my_lst[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
    except (ValueError, TypeError, IndexError):
        pass
    else:
        print()  # Adding a newline after the integers are printed.
        return count
