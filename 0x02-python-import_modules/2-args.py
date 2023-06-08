#!/usr/bin/python3

import sys

argCount = len(sys.argv) - 1

if argCount == 0:
    print("0 arguments.")
elif argCount == 1:
    print("{} arguments.".format((argCount)))
else:
    print("{} arguments:".format(argCount))

for word in range(argCount):
    print("{}: {}".format(word+1, sys.argv[word + 1]))
