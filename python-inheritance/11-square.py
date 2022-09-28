#!/usr/bin/python3
""" Module 9-rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is a class """
    def __init__(self, size):
        self.integer_validator("size", size)
        __size = size
        super().__init__(size, size)
        super().area()
