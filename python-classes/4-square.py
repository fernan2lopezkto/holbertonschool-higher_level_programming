#!/usr/bin/python3
"""an other Square"""


class Square:
    """ size = int ? """
    def __init__(self, size=0):
        if not int(size) == size:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def size(self):
        return self.__size
    
    def size(self, value):
        if not int(value) == value:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


