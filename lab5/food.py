__author__ = 'asj8139,ass7436'

"""
A module that represents the valid food types.

Author: Sean Strout @ RITCS
"""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato', 'mushroom'}  # added mushroom to food items

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato', 'mushroom'}  # added mushroom to VEGGIES

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
    'mushroom': 7  # added mushroom with calories 7
}


# Implement Food class here
class Food:
    """
        Class: Food
        Description: This class represents food item on skewer.
        Node food has 3 attributes -
        1. Name of the food
        2. Calories of that food item
        3. whether its vegan or not
        """

    __slots__ = "name", "food_calories", "is_vegan"

    def __init__(self, name):
        """
        Construct a Food instance.
        :param name: Name of the food item.
        """

        self.name = name
        self.food_calories = CALORIES[name]
        self.is_vegan = name in VEGGIES

    def is_veggie(self):
        """
        Returns the whether this food item is vegetable or not.
        :return true if food item is vegetable
                false if food item is not vegetable
        """
        return self.is_vegan
