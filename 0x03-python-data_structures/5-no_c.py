#!/usr/bin/python3
# Author: Joss


def no_c(my_string):
    noChar = ""
    for x in my_string:
        if x not in "Cc":
            noChar = noChar + x
    return(noChar)
