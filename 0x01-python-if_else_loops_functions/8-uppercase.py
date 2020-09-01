#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        values = ord(str[x])
        if (values >= 97 and values <= 122):
            values = values - 32
        print("{}".format(chr(values)), end="")
    print()
