#!/usr/bin/python3
"""Program returns the number of characters written"""


def write_file(filename="", text=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
