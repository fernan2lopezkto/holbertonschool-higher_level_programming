#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    function that append text in file
    """
    with open(filename, "a") as f:
        umb = f.write(text)

    return umb
