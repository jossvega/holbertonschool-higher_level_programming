#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(1, 10):
        if (num1 > num2 or num1 == num2):
            continue
        elif (num1 != 8):
            print("{:d}{:d}".format(num1, num2), end=', ')
        else:
            print("{:d}{:d}".format(num1, num2))
