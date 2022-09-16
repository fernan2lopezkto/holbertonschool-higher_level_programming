#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

matrix2 = [[1, 2], [4, 5], [7, 8]]

new_matrix2 = square_matrix_simple(matrix2)
print(new_matrix2)
print(matrix2)

matrixz = [[]]

new_matrixz = square_matrix_simple(matrixz)
print(new_matrixz)
print(matrixz)

matrixx = [[1], [2], [3], [4]]

new_matrixx = square_matrix_simple(matrixx)
print(new_matrixx)
print(matrixx)