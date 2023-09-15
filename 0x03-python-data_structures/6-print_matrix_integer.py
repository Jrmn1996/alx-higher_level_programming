#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for submatrix in matrix:
            if len(submatrix) == 0:
                print()
            for i in range(len(submatrix)):
                print("{:d}".format(submatrix[i]),
                      end="\n" if i == len(submatrix) - 1 else " ")
    else:
        return None