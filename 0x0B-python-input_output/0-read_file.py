#!/usr/bin/python3
"""Reads files"""


def read_file(filename=""):
    """Reads a file and prints its content"""
    with open(filename, encoding="utf-8") as text_file:
            print(text_file.read(), end="")
