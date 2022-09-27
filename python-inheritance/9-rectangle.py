#!/usr/bin/python3
""" Module 9-rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__widht = width
        self.__height = height

    def area(self):
        return self.__widht * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__widht}/{self.__height}"
