__author__ = 'asj8139,ass7436'

"""
Assignment 9: Holi Cow!
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This file represents Cow Object which has 3 properties - name, location i.e. x coordinate and y coordinate.
"""


class Cow:
    """
        Represents object Cow with color, location

        :slot: name (string):  color of the cow
        :slot: x (float):  x coordinate
        :slot: y (float):  y coordinate
    """
    __slots__ = "name", "x", "y"
    
    def __init__(self, name, x, y):
        """
        Initializes variables.
        :param name:
                Name of cow
        :param x:
                x coordinate of location
        :param y:
                y coordinate of location
        """
        self.name = name
        self.x = x
        self.y = y
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

    def __str__(self):
        """
        returns name of the cow.
        :return: name
            name of Cow
        """
        return self.name
