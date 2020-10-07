#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" Program that creates a Rectangle and intance its values """


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
