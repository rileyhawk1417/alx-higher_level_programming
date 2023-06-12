#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        print("{0}".format(" ".join([str(item) for item in items])))
    print()
