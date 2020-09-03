#!/usr/bin/python3
# Author: Joss

if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if (nargs == 0):
        print("{:d} arguments.".format(nargs))
    elif (nargs == 1):
        print("{:d} argument:".format(nargs))
    else:
        print("{:d} arguments:".format(nargs))

    for index in range(len(sys.argv)):
        if (index == 0):
            continue
        print("{:d}: {:s}".format(index, sys.argv[index]))
