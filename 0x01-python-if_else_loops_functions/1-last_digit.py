#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = abs(number)
lastNumber = result % 10

if number < 0:
    lastNumber *= -1

if lastNumber > 5:
    print("Last digit of {} is {} and is greater than 5"
        .format((number), (lastNumber)))
elif lastNumber == 0:
    print("Last digit of {} is {} and is 0"
        .format((number), (lastNumber)))
elif lastNumber < 6 and lastNumber != 0:
    print("Last digit of {} is {} "
        "and is less than 6 and not 0".format((number), (lastNumber)))

