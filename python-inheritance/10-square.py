#!/usr/bin/python3
""" Module 9-rectangle """


Rectangle = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ This is a class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
