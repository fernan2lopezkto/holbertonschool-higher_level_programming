#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    the_matrix = []
    for columna in range(len(matrix)):
        nl =[]
        for fila in range(len(matrix[0])):
            nl.append(matrix[columna][fila] ** 2)
        the_matrix.append(nl)
    return the_matrix
