#!/usr/bin/python3

def print_last_digit(number):
    addLastNumber = 0
    if number < 0:
        number *= -1
    addLastNumber = 1
    lastDigit = number % 10
    if addLastNumber == 1:
        number *= -1
    print("{:d}".format(lastDigit), end="")
    return lastDigit  # NOTE: Return keyword needed to avoid 'NONE'
