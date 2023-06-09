#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    hiddenNames = dir(hidden_4)
    print(hiddenNames)
    for findName in hiddenNames:
        if findName[:2] != '__':
            print(findName)
