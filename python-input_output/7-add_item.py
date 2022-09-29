#!/usr/bin/python3
""" module """


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_python = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    list_python.append(sys.argv[i])

save_to_json_file(list_python, "add_item.json")
