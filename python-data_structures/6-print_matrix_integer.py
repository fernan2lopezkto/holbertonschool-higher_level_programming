#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    m_len = len(matrix)
    for i in range(m_len):
        for e in range(len(matrix[i])):
            print("{:d}".format(matrix[i][e]), end="")
            if e != len(matrix[i]) - 1:
                print(end=" ")
        print()
