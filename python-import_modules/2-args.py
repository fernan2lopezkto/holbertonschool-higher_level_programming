#!/usr/bin/python3
import sys
argu = len(sys.argv)
if argu == 1:
    print("{} arguments.".format(argu - 1))
else:
    for i in range(argu):
        print("{}: {}".format(i, sys.argv[i]))