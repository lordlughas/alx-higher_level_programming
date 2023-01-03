#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer)
    """
    output = 0
    for idx in set(my_list):
        output += idx
    return (output)

