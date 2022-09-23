#!/usr/bin/python3
""" this is a 4-print_square """


def print_square(size):
    """ print_square function """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
