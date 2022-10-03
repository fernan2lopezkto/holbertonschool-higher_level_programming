#!/usr/bin/python3
"""
this is a Base class module
"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        
        if type(id) != int:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
