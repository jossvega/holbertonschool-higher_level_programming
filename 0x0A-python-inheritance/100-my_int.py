#!/usr/bin/python3
""" Program that inherits from int class """


class MyInt(int):
    """ class MyInt that inherits from int """
    def __eq__(self, other):
        """ equal (=) inverted """
        return super().__ne__(other)

    def __ne__(self, other):
        "not equal (!=) inverted """
        return super().__eq__(other)
