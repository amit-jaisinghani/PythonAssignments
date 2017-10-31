__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Food:
    __slots__ = "name", "veggie", "calories", "link"

    def __init__(self, name, veggie=False, calories=0, link=None):
        self.name = name
        self.veggie = veggie
        self.calories = calories
        self.link = link

    def __str__(self):
        description = self.name + " is a "
        if not self.veggie:
            description += " not "
        description += "vegetable with " + str(self.calories)
        return description

