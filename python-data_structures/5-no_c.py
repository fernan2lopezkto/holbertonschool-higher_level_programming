#!/usr/bin/python3
def no_c(my_string):
    for chara in my_string:
        if my_string[chara] == 'c' or my_string[chara] == 'C':
            my_string.pop(chara)
