#!/usr/bin/python3
""" script """


import json
import sys


""" import any modules """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


""" this is an onli simple script """

list_python = load_from_json_file("add_item.json")
""" convert the json a python list """

for i in range(1, len(sys.argv)):
    """ append values in arguments """
    list_python.append(sys.argv[i])

save_to_json_file(list_python, "add_item.json")
""" save new file whit new values """