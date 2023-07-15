#!/usr/bin/python3
"""Define division function for a matrix"""


errMsg = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Args:
        matrix (list): A list that has another list of ints or floats.
        div (int/float): The number to divide with.
    Raises:
        TypeError: If the matrix contains 'nan' or non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If the div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix with the result of the division.
    """
    if (
        (not isinstance(matrix, list))
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (
                isinstance(el, int) or isinstance(el, float)
                for el in [num for row in matrix for num in row]
            )
        )
    ):
        raise TypeError(errMsg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
