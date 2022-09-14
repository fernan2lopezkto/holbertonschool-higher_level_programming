#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        leter = sentence[0]
    else:
        leter = None

    return(length, leter)
