#!/usr/bin/python3


# NOTE: Have an extra list to hold uniques
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return my_list
    unique_list = []
    unique_sum = 0
    for number in my_list:
        if number not in unique_list:
            unique_list.append(number)

    for uniq in unique_list:
        unique_sum += int(uniq)
    return unique_sum
