#!/usr/bin/python3
from typing import Counter


def safe_print_list_integers(my_list=[], x=0):
    Counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            Counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return Counter
