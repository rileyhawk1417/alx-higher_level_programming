#!/bin/usr/python3

def fizzbuzz():
    for index in range(1, 100):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz", end=" ")
        elif index % 3 == 0:
            print("Fizz", end=" ")
        elif index % 5 == 0:
            print("Buzz", end=" ")
        else: 
            print("{:d}".format(index), end=" ")
