#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    list_dict = list(a_dictionary.keys())
    list_dict.sort()
    for values in list_dict:
        print("{} : {}".format(values, a_dictionary.get(values)))
