#!/usr/bin/python3
"""an other Square"""


class Square:
    def __init__(self, size=0):
        """ size = int ? """
        try:
            if type(size) != int:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be an integer")
        
        Square.size = size



