#!/usr/bin/python3

"""Defines a module for Pascal Triangle"""


def pascal_triangle(n):
    """Display Pascal's Triangle of given size
    Return a list of integers representing the Triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        tmp_list = [1]
        for idx in range(len(triangle) - 1):
            tmp_list.append(triangle[idx] + triangle[idx + 1])
        tmp_list.append(1)
        triangles.append(tmp_list)
    return triangles
