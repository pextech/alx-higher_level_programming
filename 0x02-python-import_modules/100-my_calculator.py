#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    arg_nbr = len(argv) - 1
    if arg_nbr != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op == '+':
        print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
