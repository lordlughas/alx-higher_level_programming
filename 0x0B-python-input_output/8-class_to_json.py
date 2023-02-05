#!/usr/bin/python3
"""class to JSON"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    Args:
      obj: instance of a Class (obj)
    """
    return obj.__dict__
