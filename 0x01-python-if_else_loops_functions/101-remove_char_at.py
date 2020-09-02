#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        nwstr = str[:n] + str[n + 1:]
    else:
        nwstr = str
    return (nwstr)
