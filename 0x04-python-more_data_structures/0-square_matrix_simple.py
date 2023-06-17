#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) == 0:
        return new_matrix
    """
    #NOTE:
    Well tried using for in matrix:
    loop. Didn't go as planned so inlined it
    """
    new_matrix = [[idx * idx for idx in item] for item in matrix]
    return new_matrix
