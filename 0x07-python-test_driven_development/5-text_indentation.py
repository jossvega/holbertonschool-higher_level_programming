#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    Function to print 2 new lines after '?', ':', '.'
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    newStr = text.replace('?', '?\n\n')
    newStr = newStr.replace('.', '.\n\n')
    newStr = newStr.replace(':', ':\n\n')

    print("\n".join([x.strip() for x in newStr.split("\n")]), end="")
