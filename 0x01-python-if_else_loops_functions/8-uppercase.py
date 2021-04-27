#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asci = ord(c)
        if asci >= 97 and asci < 123:
            asci = asci - 32
        print("{0:c}".format(asci), end="")
    print()
