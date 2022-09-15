#!/usr/bin/python3
if __name__ == '__main__':
    from hidden_4 import *
    lis = dir()
    for i in range(0, len(lis)):
        if lis[i][0:2] != '__':
            print(f"{lis[i]}")
