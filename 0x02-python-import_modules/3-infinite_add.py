#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argCounter = len(sys.argv) - 1
    sum = 0
    for number in range(argCounter):
        sum += int(sys.argv[number + 1])
    print("{}".format(sum))
