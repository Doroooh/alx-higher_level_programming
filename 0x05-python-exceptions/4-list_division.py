#!/usr/bin/python3

def list_division(my_lst1, my_lst2, lst_len):
    """
    Performing element-wise division between the two lists and handling exceptions.

    Args:
        my_lst1 (list): my first list.
        my_lst2 (list): my second list.
        lst_len (int): length of lists.

    Returns:
        list: A new list that contains results of element-wise division.
    """

    new = [0] * lst_len

    for k in range(lst_len):
        try:
            result = my_lst1[k] / my_lst2[k]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        else:
            new[k] = result

    return new
