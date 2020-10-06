#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return c
    elif (c > b):
        return (a + b)
    return (a * b) - c
print (magic_calculation(15, 2, 3))