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
