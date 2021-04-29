#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nmbr = len(sys.argv)
    if nmbr == 1:
        print("0 arguments.")
    elif nmbr == 2:
        print("{0:d} argument:".format(nmbr - 1))
    elif nmbr > 2:
        print("{0:d} arguments:".format(nmbr - 1))

    for i in range(len(sys.argv) - 1):
        print("{0:d}: {1:s}".format(i + 1, sys.argv[i + 1]))
