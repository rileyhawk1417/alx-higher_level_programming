#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        my_list[idx] = element
        return my_list
