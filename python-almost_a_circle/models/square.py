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

    def __str__(self):
        """ __str__ """
        a = f"[Square] ({self.id}) {self.x}/{self.height} - {self.width}"
        return a
