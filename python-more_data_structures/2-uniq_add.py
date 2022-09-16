#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqu = {}
    for number in my_list:
        uniqu[number] = number
    total = 0
    for clave in uniqu:
        total = total + clave
    return total
