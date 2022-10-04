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
        """ update function """
        item_needed = ["id", "size", "x", "y"]
        if type(args) == list:
            for item in range(len(args)):
                if item == 1:
                    setattr(self, width, args[item])
                    setattr(self, height, args[item])
                else:
                    setattr(self, item_needed[item], args[item])
                
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])