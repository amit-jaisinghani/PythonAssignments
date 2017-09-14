__author__ = 'asj8139,ass7436'

"""
Assignment 2: Day and night scene in the forest
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This is a program which draws some pictures - first of a night-time scene in a forest containing some trees, an optional
 house, and a star. The second scene will be a day-time scene of a house built from the trees, and the sun.
"""

import turtle
import random

# global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# global variables
NO_OF_TREES = 1
DRAW_HOUSE = False
IS_FIRST_TREE = True
LUMBER = 0
MAX_TREE_HEIGHT = 0


def init():
    """
        Get configurations and initialize for drawing.  (-300, -300) is in the lower left and
        (300, 300) is in the upper right.
        :pre: pos (0,0), heading (east), up
        :post: pos (0,0), heading (east), up
    :return: None
    """
    get_configurations()

    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    turtle.up()
    turtle.setheading(0)
    turtle.setpos(-250, 0)
    turtle.title('In The Forest')


def get_configurations():
    """
        Gathers user inputs for the program.
        :return: None
    """
    global NO_OF_TREES, DRAW_HOUSE
    NO_OF_TREES = int(input("How many trees do you want? "))
    if NO_OF_TREES == 1:
        DRAW_HOUSE = False
    else:
        DRAW_HOUSE = input("Do you want house? yes or no? ")
        if DRAW_HOUSE == "yes" or DRAW_HOUSE == "Yes" or DRAW_HOUSE == "YES":
            DRAW_HOUSE = True
        else:
            DRAW_HOUSE = False
    pass


def draw_path():
    """
        Draws a path
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (100,0), heading (east), up
    :return: None
    """
    global IS_FIRST_TREE
    if IS_FIRST_TREE:
        IS_FIRST_TREE = False
    else:
        turtle.down()
        turtle.forward(100)
        turtle.up()
    pass


def draw_tree_trunk(height):
    """
            Draws tree's trunk of given height
            :pre: (relative) pos (0,0), heading (east), up
            :post: (relative) pos (0, height), heading (east), up
        :return: height
    """
    turtle.setheading(90)
    turtle.down()
    turtle.forward(height)
    turtle.up()
    turtle.setheading(0)
    return height


def retain_original_position(height):
    """
        Returns to position before drawing tree.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0, -height), heading (east), up
        :return: None
    """
    turtle.setheading(270)
    turtle.down()
    turtle.forward(height)
    turtle.up()
    turtle.setheading(0)


def draw_pine_tree_leaves():
    """
        Draws tree's trunk of given height
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0, height), heading (east), up
        :return: None
    """
    side = 50
    turtle.down()
    turtle.forward(side/2)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side / 2)
    turtle.up()
    pass


def draw_maple_tree_leaves():
    """
        Draws tree's trunk of given height
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0, height), heading (east), up
        :return: None
    """
    turtle.down()
    turtle.circle(30)
    turtle.up()
    pass


def draw_box_tree_leaves():
    """
        Draws tree's trunk of given height
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0, height), heading (east), up
        :return: None
    """
    side = 50
    turtle.down()
    turtle.forward(side/2)
    for x in range(3):
        turtle.left(90)
        turtle.forward(side)
    turtle.left(90)
    turtle.forward(side/2)
    turtle.up()
    pass


def draw_tree():
    global LUMBER, MAX_TREE_HEIGHT
    draw_path()
    tree_type = random.randint(1,3)
    if tree_type == 1:
        height = draw_tree_trunk(random.randint(50, 200))
        draw_pine_tree_leaves()
        if MAX_TREE_HEIGHT < (height + 43.3):
            MAX_TREE_HEIGHT = height + 43.3
    elif tree_type == 2:
        height = draw_tree_trunk(random.randint(50, 150))
        draw_maple_tree_leaves()
        if MAX_TREE_HEIGHT < (height + 60):
            MAX_TREE_HEIGHT = height + 60
    else:
        height = draw_tree_trunk(random.randint(50, 175))
        draw_box_tree_leaves()
        if MAX_TREE_HEIGHT < (height + 50):
            MAX_TREE_HEIGHT = height + 50
    retain_original_position(height)
    LUMBER = LUMBER + height
    pass


def draw_star():
    ray_length = 10
    turtle.setposition(150, MAX_TREE_HEIGHT + 50)
    turtle.down()
    for angle in range(0, 360, 30):
        turtle.setheading(angle)
        turtle.forward(ray_length)
        turtle.back(ray_length)
    turtle.up()
    turtle.hideturtle()
    pass


def draw_house(lumber_available = 100):
    draw_path()
    turtle.down()
    turtle.forward(lumber_available)
    turtle.left(90)
    turtle.forward(lumber_available)

    turtle.left(90)
    turtle.forward(lumber_available)
    turtle.left(90)
    turtle.forward(lumber_available)
    turtle.left(90)

    turtle.forward(lumber_available)
    turtle.up()
    pass


def draw_night_scene():
    global LUMBER, DRAW_HOUSE
    if DRAW_HOUSE:
        random_house_position = random.randint(1, NO_OF_TREES - 1)
    else:
        random_house_position = -1
    for x in range(0, NO_OF_TREES):
        if x == random_house_position:
            draw_house()
        draw_tree()
    draw_star()
    pass


def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """

    init()
    draw_night_scene()
    turtle.mainloop()


if __name__ == '__main__':
    main()
