#!/usr/bin/python3
""" script """


import json
import sys


""" import any modules """


""" this is an onli simple script """

for i in range(0, len(sys.argv)):
    with open("add_item.json", "a") as f:
        f.write(json.dumps(sys.argv[i]))
