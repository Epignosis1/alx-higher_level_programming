#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    list2 = []
    for i in matrix:
        squared = []
        for elements in i:
            squared.append(elements**2)
        list2.append(squared)
    return list2
