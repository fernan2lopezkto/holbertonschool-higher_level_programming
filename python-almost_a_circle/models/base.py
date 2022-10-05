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
        """ from list to json file
        """
        list_off_dic = []

        if list_objs is not None:
            for dicti in list_objs:
                list_off_dic.append(dicti.to_dictionary())

        lis_json = json.dumps(list_off_dic)

        with open(f'{cls.__name__}.json', mode='w') as outfile:
            outfile.write(lis_json)


Base.to_json_string = staticmethod(Base.to_json_string)

Base.save_to_file = staticmethod(Base.save_to_file)
