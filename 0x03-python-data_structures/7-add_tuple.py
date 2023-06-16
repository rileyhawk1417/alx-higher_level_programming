#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    tuple_a_ = tuple_a + (0, 0)
    tuple_b_ = tuple_b + (0, 0)
    # NOTE: Figure out how to use a loop
    result = tuple_a_[0] + tuple_b_[0], tuple_a_[1] + tuple_b_[1]
    return result
