#!/usr/bin/python3
# Author: Joss


def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:s}{:d}".format(s, y), end="")
            s = " "
        print()
