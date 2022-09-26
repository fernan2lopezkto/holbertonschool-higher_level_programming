#!/usr/bin/python3
""" 4-inherith_from """


def inherits_from(obj, a_class):
    """ function """

    if a_class == object:
        return False
    else:
        return isinstance(obj, a_class)