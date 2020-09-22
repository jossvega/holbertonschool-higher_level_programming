#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as te:
        err = "Exception: " + str(te) + "\n"
        sys.stderr.write(err)
        return False
