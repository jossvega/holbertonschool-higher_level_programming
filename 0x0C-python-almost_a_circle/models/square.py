#!/usr/bin/python3
"""
Module  Square create  class Square that inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """create  class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the __str__ method that returns a custom string"""
        mssg = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
        return (mssg)

    @property
    def size(self):
        """Retriebe the size of Square"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set passet private attribute of size"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        listAttri = ["id", "size", "x", "y"]
        if (args is not None and len(args) != 0):
            for x in range(len(args)):
                if (x >= len(listAttri)):
                    break
                else:
                    setattr(self, listAttri[x], args[x])
        elif (kwargs is not None):
            for key, value in kwargs.items():
                if (key in listAttri):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        my_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return (my_dict)
