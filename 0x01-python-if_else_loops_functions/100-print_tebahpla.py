#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        asci = i
    else:
        asci = i - 32
    print("{0:c}".format(asci), end="")
