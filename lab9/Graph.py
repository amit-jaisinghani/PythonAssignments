__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""

from vertex import Vertex


class Graph:
    __slots__ = 'vertList', 'numVertices'

    def __init__(self):
        self.vertList = dict()
        self.numVertices = 0
        pass

    def addVertex(self, key):
        if key not in self.vertList.keys():
            self.vertList[key] = Vertex(key)
            self.numVertices += 1
        return self.vertList[key]

    def getVertex(self, key):
        try:
            return self.vertList[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def add_edge(self, src, dest):
        if src not in self.vertList.keys():
            self.addVertex(src)
        if dest not in self.vertList.keys():
            self.addVertex(dest)
        return self.vertList[src].add_neighbor(self.vertList[dest])

    def get_vertex_keys(self):
        return self.vertList.keys()

    def __str__(self):
        return str([str(vertex) for vertex in self.vertList.values()])

    def __iter__(self):
        return iter(self.vertList.values())
