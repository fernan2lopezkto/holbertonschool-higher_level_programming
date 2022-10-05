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

    @staticmethod
    def save_to_file(cls, list_objs):
        """ from list to json file
        """
        lista = []
        if list_objs is None:
            lista = []
        else:
            for lis in list_objs:
                lista.append(lis)
        with open(f'{cls.__name__}.json', mode='w') as outfile:
            outfile.write(lista)


Base.to_json_string = staticmethod(Base.to_json_string)
