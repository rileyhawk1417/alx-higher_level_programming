#!/usr/bin/python3


def subtract_num(roman_list):
    subtract = 0
    list_max = max(roman_list)
    for num in roman_list:
        if list_max > num:
            subtract += num
    return list_max - subtract


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    fetch_roman_keys = list(romans.keys())
    num = 0
    last_roman_num = 0
    list_roman_num = [0]

    for char in roman_string:
        for roman_num in fetch_roman_keys:
            if roman_num == char:
                if romans.get(char) <= last_roman_num:
                    num += subtract_num(list_roman_num)
                    list_roman_num = [romans.get(char)]
                else:
                    list_roman_num.append(romans.get(char))

                last_roman_num = romans.get(char)
        num += subtract_num(list_roman_num)

    return num
