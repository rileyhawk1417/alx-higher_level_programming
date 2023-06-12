#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    length = len(my_list)
    list_copy = my_list[:]
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        list_copy[idx] = element
        return list_copy
