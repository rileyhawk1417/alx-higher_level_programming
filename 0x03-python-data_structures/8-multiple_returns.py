#!/usr/bin/python3


def multiple_returns(sentence):
    tuple_result = ()
    if len(sentence) == 0:
        tuple_result = 0, "None"
    else:
        tuple_result = len(sentence), sentence[0]
    return tuple_result
