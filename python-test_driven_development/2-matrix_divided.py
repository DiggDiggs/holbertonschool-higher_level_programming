#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or any(
        not isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if each row of the matrix has the same size
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
