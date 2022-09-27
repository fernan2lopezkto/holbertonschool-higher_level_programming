#!/usr/bin/python3
""" 4-inherith_from """


def inherits_from(obj, a_class):
    """ function """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
