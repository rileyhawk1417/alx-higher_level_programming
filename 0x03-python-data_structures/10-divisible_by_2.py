#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            new_list.insert(idx, True)
        else:
            new_list.insert(idx, False)
    return new_list
