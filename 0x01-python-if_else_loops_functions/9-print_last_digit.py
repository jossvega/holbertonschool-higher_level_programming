#!/usr/bin/python3
def print_last_digit(number):
    ldigit = number % 10
    if (number < 0):
        ldigit = (number * -1) % 10
    print(ldigit, end="")
    return ldigit
