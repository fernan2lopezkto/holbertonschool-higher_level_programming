#!/usr/bin/python3
""" 1-my_list module """


class MyList(list):
    """ Mylist class, lists subclass """

    def print_sorted(self):
        print(sorted(self))
