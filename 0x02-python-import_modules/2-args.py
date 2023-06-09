#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argCount = len(sys.argv) - 1

    if argCount == 0:
        print("0 arguments.")
    elif argCount == 1:
        print("{} argument:".format((argCount)))
    else:
        print("{} arguments:".format(argCount))

    for word in range(argCount):
        print("{}: {}".format(word+1, sys.argv[word + 1]))
