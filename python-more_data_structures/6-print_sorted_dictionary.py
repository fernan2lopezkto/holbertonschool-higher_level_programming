#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_sorted = sorted(a_dictionary.items())
    a = b = 0
    for i in dic_sorted:
        print(dic_sorted[a][0], end=": ")
        print(dic_sorted[a][1])
        a += 1
