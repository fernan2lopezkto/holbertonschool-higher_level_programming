#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

def width(self):
    """ ok """
    return __width

def width(self, value):
    """ ok """
    self.__width = value

def height(self):
    """ ok """
    return self.__height

def height(self, value):
    """ ok """
    self.__height = value

def x(self):
    """ ok """
    return __x

def x(self, value):
    """ ok """
    self.__x = value

def y(self):
    """ ok """
    return __y

def y(self, value):
    """ ok """
    self.__y = value
