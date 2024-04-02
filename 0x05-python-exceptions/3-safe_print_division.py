#!/usr/bin/python3

def safe_print_division(a, b):
    """
    The code will safely perform division and print result.

    Args:
        a (float or int): numerator.
        b (float or int): denominator.

    Returns:
        float or None: Quotient if the division is successful, otherwise None.
    """

    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
