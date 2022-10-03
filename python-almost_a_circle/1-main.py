#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14)
if r is None:
    print("Can't create Rectangle")
    exit(1)



print("OK", end="")