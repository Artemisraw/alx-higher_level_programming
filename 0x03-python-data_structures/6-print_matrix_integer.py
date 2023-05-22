#!/usr/bin/python3

def print_matrix_integer(matrix=[{}]):
    if matrix is None:
        return
    for x in matrix:
        for i, value in enumerate(x):
            if i == len(x) - 1:
                print("{:d}".format(value))
            else:
                print("{:d}".format(value), end=" ")
