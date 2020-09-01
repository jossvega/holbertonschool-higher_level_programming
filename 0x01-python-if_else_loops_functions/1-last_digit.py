#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    ldigit = number % 10
else:
    ldigit = (abs(number) % 10) * -1
if (ldigit > 5):
    string = "and is greater than 5"
elif (ldigit == 0):
    string = "and is 0"
else:
    string = "and is less than 6 and not 0"
print("Last digit of", "{:d}".format(number), "is {:d}".format(ldigit), string)
