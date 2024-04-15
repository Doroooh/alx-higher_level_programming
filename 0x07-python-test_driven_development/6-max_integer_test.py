#!/usr/bin/python3
"""
Module to find the max integer in a list
"""

def max_integer(list_values=None):
    """Function to find and return the max integer in a list of integers
        If the list is empty or None, the function returns None
    """
    if not list_values:
        return None
    max_value = float('-inf')
    for value in list_values:
        if value > max_value:
            max_value = value
    return max_value
