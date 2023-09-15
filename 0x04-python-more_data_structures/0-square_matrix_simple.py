#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda smatrix: list(map(lambda x: x**2, smatrix)), matrix))
