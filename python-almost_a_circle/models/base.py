#!/usr/bin/python3
"""
this is a Base class module
"""
import json
import os
from multiprocessing import dummy
from venv import create


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

    def from_json_string(json_string):
        """ loads json string to list
        """

        if json_string is None or len(json_string) == 0:
            ls = []
            return ls
        else:
            a = json.loads(json_string)
        return a

    @classmethod
    def create(cls, **dictionary):
        """ dictionary to instance """

        if cls.__name__ == "Square":
            dummmy = cls(8)
        if cls.__name__ == "Rectangle":
            dummmy = cls(8, 8)

        dummmy.update(**dictionary)

        return dummmy

    @classmethod
    def load_from_file(cls):
        """ from file to instance """

        fil = cls.__name__ + ".json"

        if os.path.exists(fil):
            with open(fil, "r") as f:
                m = f.read()
                n = cls.from_json_string(m)
                asa = []
                for inst in range(len(n)):
                    a = n[inst]
                    asa.append(cls.create(**a))
                return asa
        else:
            return []

Base.to_json_string = staticmethod(Base.to_json_string)
