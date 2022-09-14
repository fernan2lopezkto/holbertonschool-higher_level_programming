#!/usr/bin/python3
from audioop import reverse


def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    while idx >= 0:
        print("{:d}".format(my_list[idx]))
        idx = idx - 1
