#!/usr/bin/python3

import hidden_4

hiddenNames = dir(hidden_4)
# BUG: This still fails why?
print(hiddenNames)
for findName in hiddenNames:
    if findName[:2] != '__':
        print(findName)
