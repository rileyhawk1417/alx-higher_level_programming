#!/usr/bin/python3
"""
NOTES: IndexError is useful when using it with for loops
"""


def safe_print_list(my_list=[], x=0):
    returnValue = 0
    for items in range(x):
        try:
            print("{}".format(my_list[items]), end="")
            returnValue += 1
        except IndexError:
            break
    print("")
    return returnValue
