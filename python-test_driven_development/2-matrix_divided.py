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
    a = len(matrix[0])
    for columna in range(len(matrix)):
        if len(matrix[columna]) != a:
            raise TypeError("Each row of the matrix must have the same size")
        nl = []
        for fila in range(len(matrix[0])):
            if type(matrix[columna][fila]) == int or type(matrix[columna][fila]) == float:
                nl.append(round(matrix[columna][fila] / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        the_matrix.append(nl)

    return the_matrix
