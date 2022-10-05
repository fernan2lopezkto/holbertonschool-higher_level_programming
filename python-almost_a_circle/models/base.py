#!/usr/bin/python3
"""
this is a Base class module
"""
import json


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

    def to_json_string(list_dictionaries):
        """ list to json strings
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            a = json.dumps(list_dictionaries)
        return a

    def save_to_file(cls, ):
        """ from list to json file
        """
        with open(f'{self.__class__.__name__}.json', 'w') as outfile:
            json.dump(letters, outfile)


Base.to_json_string = staticmethod(Base.to_json_string)
