#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor function """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """
    -- propertis --
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
    -- seters --
    """

    @width.setter
    def width(self, value):
        """ set width """
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x """
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        self.__y = value
