#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # NOTE:Only print items in list range
    for items in range(len(my_list)):
        print("{:d}".format(my_list[items]))
