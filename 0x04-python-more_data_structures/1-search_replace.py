#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    new_list = my_list[:]

    for item in range(len(new_list)):
        if new_list[item] == search:
            new_list[item] = replace
    return new_list
