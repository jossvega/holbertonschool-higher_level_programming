#!/usr/bin/python3
"""Program that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return (count)
