__author__ = 'asj8139,ass7436'

"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
"""


class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """

    __slots__ = "item", "next"

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """

        self.item = item
        self.next = next
        pass

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        size = 0
        n = self
        while n is not None:
            size += 1
            n = n.next
        return size

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.
        """
        only_veggies = True
        n = self
        while n is not None:
            if not n.item.is_veggie():
                only_veggies = False
                break
            n = n.next
        return only_veggies

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        has_item = False
        n = self
        while n is not None:
            if name == n.item.name:
                has_item = True
                break
            n = n.next
        return has_item

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """

        list_of_items = self.item.name
        n = self.next
        while n is not None:
            list_of_items = list_of_items + ', ' + n.item.name
            n = n.next
        return list_of_items

    def total_calorie_count(self):
        """
        Returns the total calories count of food items on the skewer.
        :return total calories
        """
        calories = 0
        n = self
        while n is not None:
            calories += n.item.food_calories
            n = n.next
        return calories

    def get_item(self):
        """
        Returns the item (food) in this kebab spot.
        :return item (food)
        """
        return self.item
