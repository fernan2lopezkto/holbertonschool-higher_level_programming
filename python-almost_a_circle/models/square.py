#!/usr/bin/python3
"""
square module from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ use width and height property """
        self.width = value
        self.height = value

    def __str__(self):
        """ whow width and heath """
        a = f"[Square] ({self.id}) {self.x}/{self.y}"
        b = f" - {self.width}"
        return a + b

    def update(self, *args, **kwargs):
        """ update function
        """

        length = len(args)

        if length > 0:
            self.id = args[0]
        if length > 1:
            self.size = args[1]
        if length > 2:
            self.x = args[2]
        if length > 3:
            self.y = args[3]
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ return self atribut in dinctionary """
        item_needed = ["id", "size", "x", "y"]
        self_atrib = self.__dict__
        filt_atrib = {}

        for itm in range(len(self_atrib)):
            filt_atrib[item_needed[itm]] = getattr(self, item_needed[itm])

        return filt_atrib