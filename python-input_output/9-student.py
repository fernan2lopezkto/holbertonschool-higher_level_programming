#!/usr/bin/python3
""" 9-sudent class module """


class Student:
    """ this is a super class """
    def __init__(self, first_name, last_name, age):
        """ init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return self atribut in dinctionary """
        return self.__dict__
