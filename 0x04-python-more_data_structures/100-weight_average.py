#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = items = 0
    for (x, y) in my_list:
        total = total + (x * y)
        items = items + y
    return total / items
