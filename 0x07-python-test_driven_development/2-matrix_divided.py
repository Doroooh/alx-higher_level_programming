#!/usr/bin/python3
"""
This is the matrix_divided module.

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Divide each element of the matrix by the given divisor and return a new matrix.

    Args:
        matrix (list): List of lists containing integers or floats.
        div (int, float): The divisor, must be a number and not zero.

    Returns:
        list: A new matrix with each element divided by the divisor.
    """
    # Error messages
    mtrx_type_e = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_len_e = 'Each row of the matrix must have the same size'
    div_type_e = 'div must be a number'
    div_zero_e = 'division by zero'

    # Check if the matrix is a valid list of lists
    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_e)

    # Iterate through each row of the matrix
    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_e)
        # Check if each element in the row is an integer or float
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_e)
        # Check if each row has the same length
        if len(row) != row_len and row_len != 0:
            raise TypeError(mtrx_len_e)
        row_len = len(row)

    # Check if the divisor is a number and not zero
    if type(div) not in [int, float]:
        raise TypeError(div_type_e)
    if div == 0:
        raise ZeroDivisionError(div_zero_e)

    # Divide each element of the matrix by the divisor and round to 2 decimal places
    return [[round(nb / div, 2) for nb in row] for row in matrix]
