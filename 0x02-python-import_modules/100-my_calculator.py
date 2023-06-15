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

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops(operator)))
