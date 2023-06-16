#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list is None:
        return "None"
    else:
        # NOTE: Just assign the first value
        # NOTE: If theres a number higher then assign it
        max = my_list[0]
        for index in range(len(my_list)):
            if my_list[index] > max:
                max = my_list[index]
        return max
