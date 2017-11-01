from Food import Food

__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Skewer:
    __slots__ = "top"

    def __init__(self):
        self.top = None

    def __str__(self):
        result = "Skewer["
        n = self.top
        while n is not None:
            result += " " + str(n) + "\n"
            n = n.link
        result += " ]"
        return result

    def is_empty(self):
        return self.top is None

    def push(self, food_name, is_vegetable, calories):
        self.top = Food(food_name, is_vegetable, calories, self.top)

    def pop(self):
        assert not self.is_empty(), "Pop from empty skewer"
        self.top = self.top.link

    def peek(self):
        assert not self.is_empty(), "peek on empty skewer"
        return self.top

    def is_veggie(self):
        only_veggies = True
        if not self.is_empty():
            n = self.top
            while n is not None:
                if not n.veggie:
                    only_veggies = False
                    break
                n = n.link
            return only_veggies


def main():
    s = Skewer()
    s.push("potato", True, 100)
    s.push("Onion", True, 10)
    s.push("Chicken", False, 1500)
    print(s)
    print("Checking all veg --")
    print("is veg? ", s.is_veggie())
    s.pop()
    print(s)
    print("is veg? ", s.is_veggie())


if __name__ == "__main__":
    main()
