#!/usr/bin/python3


def common_elements(set_1, set_2):
    if len(set_1) == 0:
        return set_1
    if len(set_2) == 0:
        return set_2

    for item_a in set_1:
        if item_a in set_2:
            return item_a
