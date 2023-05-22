#!/usr/bin/python3

"""if __name__ == "__main__":"""
def square_matrix_simple(matrix=[]):
    for x in matrix:
        for i in range(len(x)):
            x[i] **= 2
    result = [list(x) for x in matrix]
    return result
