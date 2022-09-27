#!/usr/bin/python3
""" 5-base_geometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
