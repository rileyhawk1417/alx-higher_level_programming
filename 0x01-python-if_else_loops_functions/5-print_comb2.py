#!/usr/bin/python3
for i in range(0, 99):
    print("{}{}".format((i // 10), (i % 10)), end=", ")
    i += 1
print("{}".format(99))
