#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divide the two list elements individually
    Args:
        my_list_1 (list): The first list
        my_list_2 (list): The second list
        list_length (int): The list length
    Returns:
        A new list containing all the divisions
    """
    result = 0
    new_list = []
    for items in range(0, list_length):
        try:
            result = my_list_1[items] / my_list_2[items]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
