#!/usr/bin/python3
""" func"""

def add_integer(a, b=98):
    """func"""
    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")

    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")