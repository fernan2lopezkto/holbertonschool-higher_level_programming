#!/usr/bin/python3
""" 2-matrix_divided modul """


def matrix_divided(matrix, div):
    """function to divide all matrix elements"""
    if type(div) != int:
        if type(div) != float:
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    the_matrix = []
    textE = "matrix must be a matrix (list of lists) of integers/floats"
    a = len(matrix[0])
    for c in range(len(matrix)):
        if len(matrix[c]) != a:
            raise TypeError("Each row of the matrix must have the same size")
        nl = []
        for fila in range(len(matrix[0])):
            if type(matrix[c][fila]) == int or type(matrix[c][fila]) == float:
                nl.append(round(matrix[c][fila] / div, 2))
            else:
                raise TypeError(textE)
        the_matrix.append(nl)

    return the_matrix

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")