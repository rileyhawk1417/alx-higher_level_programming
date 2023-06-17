#!/usr/bin/python3


def number_keys(a_dictionary):
    if len(a_dictionary) == 0:
        return a_dictionary
    return len(list(a_dictionary.keys()))
