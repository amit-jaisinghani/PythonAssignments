__author__ = 'asj8139,ass7436'

"""
Assignment 9: Holi Cow!
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This file represents PaintBall Object which has 4 properties - name, blast radius, location i.e. x coordinate and y coordinate.
"""


class PaintBall:
    """
        Represents object Paint Ball with color, location and blast radius

        :slot: name (string):  color of the paint ball
        :slot: x (float):  x coordinate
        :slot: y (float):  y coordinate
        :slot: blast radius (string): blast radius of paint ball
    """
    __slots__ = "name", "x", "y", "blast_radius"

    def __init__(self, name, x, y, blast_radius):
        """
        Initializes variables.
        :param name:
                Name of cow
        :param x:
                x coordinate of location
        :param y:
                y coordinate of location
        :param blast_radius:
                blast radius of the paint ball
        """
        self.name = name
        self.x = x
        self.y = y
        self.blast_radius = blast_radius
        pass

    def getX(self):
        """
            converts x coordinate of location to float and returns it.
            :return: x coordinate
                    float type of x coordinate of location
        """
        return float(self.x)

    def getY(self):
        """
            converts y coordinate of location to float and returns it.
            :return: y coordinate
                    float type of y coordinate of location
        """
        return float(self.y)

    def getBlastRadius(self):
        """
            converts blast radius of paint ball to float and returns it.
            :return: blast radius
                        float type of blast radius of paint ball
        """
        return float(self.blast_radius)

    def __str__(self):
        """
            returns color of the paint ball.
            :return: name
                color of the paint ball
        """
        return self.name
