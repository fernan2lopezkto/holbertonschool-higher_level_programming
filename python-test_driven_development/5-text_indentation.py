#!/usr/bin/python3
""" 5-text_identation module """


def text_indentation(text):
    """ text_identation function """

    for letra in range(len(text)):
        print(text[letra], end="")
        if text[letra - 1] == "." or text[letra - 1]  == "?" or text[letra - 1]  == ":":
            print()
            print()

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
