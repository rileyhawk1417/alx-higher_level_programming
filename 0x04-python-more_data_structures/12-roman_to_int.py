#!/usr/bin/python3
"""
NOTE: Well in order to get this right
Count the letters from the right. <-
For example "IV"  V is 5 & I is 1
Since the "I" is before the "V" we subtract
giving us 4. However if the I were after V
it would give us 6
"""


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    _dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    string_len = len(roman_string)
    index = string_len - 1
    result = 0
    while index >= 0:
        if (
            index < string_len - 1
            and _dict[roman_string[index]] < _dict[roman_string[index + 1]]
        ):
            result -= _dict[roman_string[index]]
        else:
            result += _dict[roman_string[index]]
        index -= 1
    return result
