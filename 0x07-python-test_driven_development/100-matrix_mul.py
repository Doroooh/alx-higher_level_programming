#!/usr/bin/python3
"""
This is the matrix_mul_7a1d module.

This module supplies one function, matrix_mul_7a1d().
"""


def matrix_mul_7a1d(matrix_a, matrix_b):
    """
    Return a new matrix resulting from the multiplication of two matrices.

    Args:
        matrix_a (list): List of lists containing integers or floats.
        matrix_b (list): List of lists containing integers or floats.

    Returns:
        list: Resulting matrix from the multiplication.
    """
    # Validation checks
    if not isinstance(matrix_a, list) or not isinstance(matrix_b, list):
        raise TypeError("Both matrix_a and matrix_b must be lists")
    
    if not all(isinstance(row, list) for row in matrix_a) or not all(isinstance(row, list) for row in matrix_b):
        raise TypeError("Both matrix_a and matrix_b must be lists of lists")
    
    if any(not row for row in matrix_a) or any(not row for row in matrix_b):
        raise ValueError("Both matrix_a and matrix_b must contain non-empty lists")
    
    if any(not all(isinstance(element, (int, float)) for element in row) for row in matrix_a) or \
       any(not all(isinstance(element, (int, float)) for element in row) for row in matrix_b):
        raise TypeError("Both matrix_a and matrix_b must contain only integers or floats")
    
    if any(len(row) != len(matrix_a[0]) for row in matrix_a) or \
       any(len(row) != len(matrix_b[0]) for row in matrix_b):
        raise TypeError("All rows in both matrix_a and matrix_b must have the same length")
    
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("The number of columns in matrix_a must be equal to the number of rows in matrix_b")
    
    # Matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)] for row_a in matrix_a]
    
    return result
