#!/usr/bin/python3

def print_matrix_integer(matrix = [{}]):
    for x in matrix:
        for i in x:
            print(" {}".format(i), end="")
        print()
