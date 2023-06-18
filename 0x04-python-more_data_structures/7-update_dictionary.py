#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
        return []
    if key not in a_dictionary.items() or key in a_dictionary.items():
        a_dictionary[key] = value
    return a_dictionary
