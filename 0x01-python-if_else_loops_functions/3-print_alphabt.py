
#!/usr/bin/python3
for i in range(97, 123):
    if i != ord('q') and i != ord('e'):
        print("{0:c}".format(i), end="")
