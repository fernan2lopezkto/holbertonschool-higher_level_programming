#!/usr/bin/python3
""" class Rectangle module """


from models.base import Base


class Rectangle(Base):
    """ rectangle class inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


def width(self):
    return __width

def width(self, value):
    self.__width = value

def height(self):
    return self.__height

def height(self, value):
    self.__height = value

def x(self):
    return __x

def x(self, value):
    self.__x = value

def y(self):
    return __y

def y(self, value):
    self.__y = value
