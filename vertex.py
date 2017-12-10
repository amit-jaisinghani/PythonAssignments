__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

An implementation of a vertex as part of a graph.

Code taken from lecture code and modified:
"""


class Vertex:
    """
        An individual vertex in the graph.

        :slots: id:  The identifier for this vertex (user defined, typically
            a string)
        :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
            the neighbor (Vertex)
    """
    __slots__ = "key", "connected_to"

    def __init__(self, key):
        """
            Initialize a vertex
            :param key: The identifier for this vertex
            :return: None
        """
        self.key = key
        self.connected_to = []

    def add_neighbor(self, neighbor):
        """
            Connect this vertex to a neighbor with a given weight (default is 0).
            :param nbr (Vertex): The neighbor vertex
            :param weight (int): The edge cost
            :return: None
        """
        self.connected_to.append(neighbor)

    def __str__(self):
        """
            Return a string representation of the vertex and its direct neighbors:

                vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

            :return: The string
        """
        return str(self.key) + " connectedTo: " + str(
            [str(x.key) for x in self.connected_to])

    def get_connections(self):
        """
            Get the neighbor vertices.
            :return: A list of Vertex neighbors
        """
        return self.connected_to

    def __eq__(self, other):
        """
        Compare this vertex with other vertex based on the key of vertex.
        :param other:
                another vertex to compare.
        :return: True; if vertexes keys are same
                 False; if vertexes keys are different
        """
        return self.key == other.key

    def __ne__(self, other):
        """
            Compare this vertex with other vertex based on the key of vertex.
            :param other:
                    another vertex to compare.
            :return: True; if vertexes keys are different
                     False; if vertexes keys are same
        """
        return self.key != other.key

    def __hash__(self):
        """
        Returns hash value of key
        :return: Hash value
        """
        return hash(self.key)
