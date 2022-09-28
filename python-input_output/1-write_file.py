#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    function to write in file
    """
    with open(filename, "w") as f:
        n_l = f.write(text)

    return n_l
