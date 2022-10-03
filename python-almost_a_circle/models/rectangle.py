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

@property
def get_width(self):
    """ gett width """
    return self.__width


@property
def get_height(self):
    """ gett width """
    return self.__height

@get_width.setter
def set_width(self, value):
    """ set width """
    self.__width = value
