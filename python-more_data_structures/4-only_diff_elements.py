#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_y = set_1 & set_2
    set_mas = set_1 | set_2
    set_r = set_mas - set_y
    return set_r
