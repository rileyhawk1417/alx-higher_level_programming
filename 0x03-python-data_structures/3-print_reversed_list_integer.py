#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for items in range(length, 0, -1):
        print("{}".format(items))
