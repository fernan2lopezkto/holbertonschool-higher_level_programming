#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

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
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        type_error("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x """
        type_error("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        type_error("y", value)
        self.__y = value

    """ 
    ---------------
    -- to errors --
    ---------------
    """

def type_error(name, value2):
    """ chek type """
    if type(value2) != int:
        raise TypeError(f"{name} must be an integer")
