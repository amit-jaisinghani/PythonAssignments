__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Color:
    __slots__ = "name", "x", "y", "blast_radius"

    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return self.name
