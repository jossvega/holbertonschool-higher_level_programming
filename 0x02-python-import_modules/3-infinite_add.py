#!/usr/bin/python3
# Author: Joss
if __name__ == "__main__":
    import sys

    sum = 0

    for index in range(len(sys.argv)):
        if (index == 0):
            continue
        else:
            sum += int(sys.argv[index])
    print("{}".format(sum))
