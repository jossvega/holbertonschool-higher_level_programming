#!/usr/bin/python3
"""
dvfdvfdfvbda
"""


class Base:
    """
    First class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
