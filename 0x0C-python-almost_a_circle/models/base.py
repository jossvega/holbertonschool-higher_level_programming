#!/usr/bin/python3
"""
Base class of all other classes in this project
"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        my_list = []
        fname = cls.__name__ + ".json"
        if (list_objs is not None):
            for indx in list_objs:
                my_list.append(indx.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, "w") as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if (json_string is None or len(json_string) == 0):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set """
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        my_list = []
        fname = cls.__name__ + ".json"
        if os.path.isfile(fname):
            with open(fname, "r") as f:
                stread = f.read()
                listjson = cls.from_json_string(stread)
                for a in listjson:
                    my_list.append(cls.create(**a))
        return (my_list)
