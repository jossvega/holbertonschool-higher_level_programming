#!/usr/bin/python3
"""
Module rectangle Create a Rectangle class, inheriting from Base.
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retriebe the width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set passet private attribute of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Set passed private attribute of height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set private instance attribute x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve private instance sttribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set private instance attribute y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character # """
        for y in range(self.y):
            print()
        for x in range(self.height):
            print(" " * self.x, end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overriding the __str__ method that returns a custom string"""
        mssg = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        return (mssg)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        listAttri = ["id", "width", "height", "x", "y"]

        if (args and len(args) != 0):
            for argItem in range(len(args)):
                if (argItem == 0):
                    super().__init__(args[argItem])
                elif (argItem < len(listAttri)):
                    setattr(self, listAttri[argItem], args[argItem])
        else:
            for key, value in kwargs.items():
                if (key == "id"):
                    super().__init__(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        my_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return (my_dict)
