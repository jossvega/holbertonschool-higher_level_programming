#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute


class MyClass():
    pass


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
print(dir(mc))
print()
print(dir(a))
print()


"""Advanced 100
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
"""

"""Task 10 Square = __import__('10-square').Square
and 11
-----
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
"""

"""Task 9
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
print(dir(Rectangle))
"""

"""Task 8
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""

"""Task 7
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)


try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("caro", 100.2)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""


"""Task 6
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""

"""Task 4
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

b = False
if inherits_from(b, int):
    print("{} inherited from class {}".format(b, int.__name__))
if inherits_from(b, bool):
    print("{} inherited from class {}".format(b, bool.__name__))
if inherits_from(b, object):
    print("{} inherited from class {}".format(b, object.__name__))
"""

"""Task 3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
"""

"""Task 2
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
"""

"""Task 1
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
"""

"""Task 0
lookup = __import__('0-lookup').lookup
class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


print(lookup(MyClass1))
print()
print(lookup(MyClass2))
print()
print(lookup(int))
"""
