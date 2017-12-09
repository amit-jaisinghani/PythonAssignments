__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Vertex:
    __slots__ = "key", "connected_to"

    def __init__(self, key):
        self.key = key
        self.connected_to = []

    def add_neighbor(self, neighbor):
        self.connected_to.append(neighbor)

    def __str__(self):
        return str(self.key) + "->" + str(
            [str(x.key) for x in self.connected_to])

    def get_connections(self):
        return self.connected_to

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __hash__(self):
        return hash(self.key)
