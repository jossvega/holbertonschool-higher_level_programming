#!/usr/bin/python3
"""Program that define a Student with filter"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        dic = {}
        if attrs is not NONE:
            return (self.__dict__)
        else:
            for x in attrs:
                if hasattr(self, x):
                    dic[x] = getattr(self, x)
            return (dic)
