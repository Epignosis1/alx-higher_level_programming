#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_set = set(my_list)
    number_list = list(my_set)
    add = 0
    for i in new_set:
        add = add + i
    return add

