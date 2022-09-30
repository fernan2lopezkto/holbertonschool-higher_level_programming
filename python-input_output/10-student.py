#!/usr/bin/python3
""" 9-sudent class module """


class Student:
    """ this is a super class """
    def __init__(self, first_name, last_name, age):
        """ init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return self atribut in dinctionary """
        if attrs:
            filt_atrib = {}
            self_atrib = self.__dict__
            for itm in attrs:
                if hasattr(self, itm):
                    filt_atrib[itm] = getattr(self, itm, "")
            return filt_atrib

        return self.__dict__
