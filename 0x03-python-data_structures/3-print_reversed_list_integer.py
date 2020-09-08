#!/usr/bin/python3
# Author: Joss


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return(None)
    for list in reversed(my_list):
        print("{:d}".format(list))
