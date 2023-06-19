#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    division = 0
    total = 0
    for left, right in my_list:
        total += left * right
        division += right
    return total / division
