#!/usr/bin/python3
""" 8-class_to_json """


import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)