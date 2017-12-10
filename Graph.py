__author__ = 'asj8139,ass7436'

"""
Assignment 9: Holi Cow!
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

An implementation of a graph data structure as an adjacency list.

Code taken from lecture code and modified.
"""

from vertex import Vertex


class Graph:
    """
        A graph implemented as an adjacency list of vertices.

        :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
            object
        :slot: numVertices (int):  The total number of vertices in the graph
    """
    __slots__ = 'vertList', 'numVertices'

    def __init__(self):
        """
            A graph implemented as an adjacency list of vertices.

            :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
                object
            :slot: numVertices (int):  The total number of vertices in the graph
        """
        self.vertList = dict()
        self.numVertices = 0
        pass

    def addVertex(self, key):
        """
          Add a new vertex to the graph.
          :param key: The identifier for the vertex (typically a string)
          :return: Vertex
        """
        if key not in self.vertList.keys():
            self.vertList[key] = Vertex(key)
            self.numVertices += 1
        return self.vertList[key]

    def getVertex(self, key):
        """
            Retrieve the vertex from the graph.
            :param key: The vertex identifier
            :return: Vertex if it is present, otherwise None
        """
        try:
            return self.vertList[key]
        except KeyError:
            return None

    def __contains__(self, key):
        """
            Returns whether the vertex is in the graph or not.  This allows the
            user to do:

                key in graph

            :param key: The vertex identifier
            :return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def addEdge(self, src, dest):
        """
            Add a new directed edge from a source to a destination of an edge cost.
            :param src: The source vertex identifier
            :param dest: The destination vertex identifier
            :param cost: The edge cost (defaults to 0)
            :return: None
        """
        if src not in self.vertList.keys():
            self.addVertex(src)
        if dest not in self.vertList.keys():
            self.addVertex(dest)
        return self.vertList[src].add_neighbor(self.vertList[dest])

    def get_vertex_keys(self):
        """
            Return the collection of vertex identifiers in the graph.
            :return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __str__(self):
        """
        Return a string representation of all vertex in the graph and their direct neighbors:

        :return: The string
        """
        return str([str(vertex) for vertex in self.vertList.values()])

    def __iter__(self):
        """
            Return an iterator over the vertices in the graph.  This allows the
            user to do:

                for vertex in graph:
                    ...

            :return: A list iterator over Vertex objects
        """
        return iter(self.vertList.values())
