#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import calculator_1


def ops(operator):
    if operator == "+":
        return calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
    if operator == "-":
        return calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
    if operator == "*":
        return calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
    if operator == "/":
        return calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


print("{} {} {}".format(sys.argv[1], sys.argv[2], sys.argv[3]), end="")
print(" = {}".format(ops(sys.argv[2])))
