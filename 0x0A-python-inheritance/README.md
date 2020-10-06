# 0x0A. Python - Inheritance
---
## Description
Repository to study the following Python topics: Inheritance

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Task Project
---
File Name|Task Name|Task Description
---|---
0 - Lookup|Write a function that returns the list of available attributes and methods of an object:
1 - My list|Write a class MyList that inherits from list
2 - Exact same object|Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
3 - Same class or inherit from|Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
4 - Only sub class of|Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
5 - Geometry module|Write an empty class BaseGeometry.
6 - Improve Geometry|Write a class BaseGeometry (based on 5-base_geometry.py).raises an Exception with the message area() is not implemented
7 - Integer validator|Write a class BaseGeometry (based on 6-base_geometry.py).Public instance method: def integer_validator(self, name, value): that validates value:
8 - Rectangle|Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).Instantiation with width and height: def __init__(self, width, height):
9 - Full rectangle|Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)Print area and string personalize format
10 - Square #1|Write a class Square that inherits from Rectangle (9-rectangle.py):
11 - Square #2|Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).