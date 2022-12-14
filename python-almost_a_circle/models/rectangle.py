#!/usr/bin/python3
""" rectangle module """
from multiprocessing.sharedctypes import Value
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    the_picsel = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor function """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """
    ---------------
    -- propertis --
    ---------------
    """

    @property
    def width(self):
        """ gett width """
        return self.__width

    @property
    def height(self):
        """ gett width """
        return self.__height

    @property
    def x(self):
        """ gett x """
        return self.__x

    @property
    def y(self):
        """ gett y """
        return self.__y

    """
    ------------
    -- seters --
    ------------
    """

    @width.setter
    def width(self, value):
        """ set width """
        type_error("width", value)
        wh("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        type_error("height", value)
        wh("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x """
        type_error("x", value)
        xy("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        type_error("y", value)
        xy("y", value)
        self.__y = value

    """
    -----------=-
    -- methods --
    ----------=--
    """

    def area(self):
        """
        The function area() calculates the area of a rectangle
        :return: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self):
        """ whow width and heath """
        a = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        b = f" - {self.width}/{self.height}"
        return a + b

    def display(self):
        """ print rectangle """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            string = ''
            for m in range(0, self.__y):
                string += '\n'
            for i in range(self.__height):
                if i > 0:
                    string += '\n'
                for k in range(0, self.__x):
                    string += ' '
                for j in range(self.__width):
                    string += str(self.the_picsel)
            print(string)

    def update(self, *args, **kwargs):
        """ update function """
        item_needed = ["id", "width", "height", "x", "y"]
        if type(args) == list:
            for item in range(len(args)):
                setattr(self, item_needed[item], args[item])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ return self atribut in dinctionary """
        item_needed = ["id", "width", "height", "x", "y"]
        self_atrib = self.__dict__
        filt_atrib = {}

        for itm in range(len(self_atrib)):
            filt_atrib[item_needed[itm]] = getattr(self, item_needed[itm])

        return filt_atrib

"""
---------------
-- to errors --
---------------
"""


def type_error(name, value2):
    """ chek type """
    if type(value2) != int:
        raise TypeError(f"{name} must be an integer")


def wh(name, value3):
    """ check value of width and height """
    if value3 <= 0:
        raise ValueError(f"{name} must be > 0")


def xy(name, value4):
    """ check value of x and y """
    if value4 < 0:
        raise ValueError(f"{name} must be >= 0")
