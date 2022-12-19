#!/usr/bin/python3
<<<<<<< HEAD
# 3-print_reversed_list_integer.py
=======
#print_reversed_list_integer.py
>>>>>>> 6298629b205210e7dae24b1ec46807aeeea58dc5


def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for val in my_list:
            print("{:d}".format(val))
