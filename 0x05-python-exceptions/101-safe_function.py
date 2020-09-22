#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as te:
        err = "Exception: " + str(te) + "\n"
        sys.stderr.write(err)
        return (None)
    return (result)
