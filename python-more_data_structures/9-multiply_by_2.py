#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_2 = {}
    for clave in a_dictionary:
        a_2[clave] = a_dictionary[clave] * 2
    return a_2
