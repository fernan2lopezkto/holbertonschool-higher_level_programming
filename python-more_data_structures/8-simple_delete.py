#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    there_is = False
    for clave in a_dictionary:
        if clave == key:
            there_is = True
    if there_is:
        a_dictionary.pop(key)
    return a_dictionary
