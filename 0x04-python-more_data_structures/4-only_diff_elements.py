#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_list = []
    if len(set_1) == 0:
        return set_1
    if len(set_2) == 0:
        return set_2

    for item_a in set_2:
        if item_a not in set_1:
            new_list.append(item_a)
    for item_b in set_1:
        if item_b not in set_2:
            new_list.append(item_b)
    return new_list
