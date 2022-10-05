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

    @classmethod
    def save_to_file(cls, list_objs):
        """ objets to json file """

        fil = cls.__name__ + ".json"

        with open(fil, "w") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            lis = []

            for dic in list_objs:
                lis.append(dic.to_dictionary())

            return f.write(cls.to_json_string(lis))


Base.to_json_string = staticmethod(Base.to_json_string)
