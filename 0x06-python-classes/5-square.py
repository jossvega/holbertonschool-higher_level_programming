#!/usr/bin/python3
"""
Square Class: Define a Square with private instance
"""


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0):
        """ initialize variables """
        self.__size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ste the size with safe Assigment"""
        if type(value) is not int:
            raise TypeError("size must be a integer")
        if (value < 0):
            raise ValueError("size mustbe >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if (self.size is not 0):
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
