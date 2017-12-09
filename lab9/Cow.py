__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Cow:
    
    __slots__ = "name", "x", "y"
    
    def __init__(self, name):
        self.name = name
        pass
    
    def __str__(self):
        return self.name
