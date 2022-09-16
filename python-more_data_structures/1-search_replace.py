#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_lii = []
    for number in my_list:
        if number == search:
            my_lii.append(replace)
        else:
            my_lii.append(number)
    return my_lii
