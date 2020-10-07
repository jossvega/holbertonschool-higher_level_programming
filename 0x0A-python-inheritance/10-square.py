#!/usr/bin/python3
"""
A class Square that inherits from Rectangle from BaseGeometry.
"""


Rectangle = __import__("9-rectangle").Rectangle


"""Program that creates a Square and intance its values"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Constructor maping size to parent constructor"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Finds the area of a square, using inheritance of rectangle"""
        return super().area()
