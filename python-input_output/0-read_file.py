#!/usr/bin/python3
""" 0-read file module """


def read_file(filename=""):
    """
    function to read and print file lines
    """
    with open(filename) as f:
        read_data = f.read()

    for line in read_data:
        print(line, end="")
