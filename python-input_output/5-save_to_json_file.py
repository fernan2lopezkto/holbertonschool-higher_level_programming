#!/usr/bin/python3
""" 5-save_to_json_file module """


import json


def save_to_json_file(my_obj, filename):
    """ save to json file """

    with open(filename, "w+") as f:
        f.write(json.dumps(my_obj))
