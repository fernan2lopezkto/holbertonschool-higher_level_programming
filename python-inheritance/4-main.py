#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from


class Be:
    pass

a = True
b = Be

if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(b, object):
    print("{} inherited from class {}".format(a, object.__name__))
