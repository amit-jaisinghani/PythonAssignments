__author__ = 'asj8139,ass7436'

"""
Assignment 2: Day and night scene in the forest
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This is a program which draws some pictures - first of a night-time scene in a forest containing some trees, an optional
 house, and a star. The second scene will be a day-time scene of a house built from the trees, and the sun.
"""

import turtle
import random
import math

# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


def init():
    """
        Initialize for drawing.  (-400, -400) is in the lower left and
        (400, 400) is in the upper right.
        :pre: pos (0,0), heading (east), up
        :post: pos (0,0), heading (east), down
        :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    turtle.up()
    turtle.setheading(0)
    turtle.setpos(-250, 0)
    turtle.title('In The Forest')


def get_configurations():
    """
        Gathers user inputs for the program.
        :return: no_of_trees, house_required
    """
    no_of_trees = int(input("How many trees in your forest? "))
    if no_of_trees <= 1:
        house_required = False
    else:
        house_required_input = input("Is there a house in the forest (y/n)? ")
        if house_required_input == "yes" or house_required_input == "Yes" or house_required_input == "YES" or house_required_input == "y":
            house_required = True
        else:
            house_required = False
    return no_of_trees, house_required


def draw_path():
    """
        Draws a path
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (100,0), heading (east), up
        :return: None
    """
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
        Draws equilateral triangle of side 50
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
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
        Draws a circle of radius 30
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """
    turtle.down()
    turtle.circle(30)
    turtle.up()
    pass


def draw_box_tree_leaves():
    """
        Draws a square of side 50
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
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
    """
        Draws a tree with trunk and leaves
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: tree_height, trunk_height
    """
    tree_type = random.randint(1,3)

    if tree_type == 1:
        trunk_height = draw_tree_trunk(random.randint(50, 200))
        draw_pine_tree_leaves()
        tree_height = trunk_height + 43.3
    elif tree_type == 2:
        trunk_height = draw_tree_trunk(random.randint(50, 150))
        draw_maple_tree_leaves()
        tree_height = trunk_height + 60
    else:
        trunk_height = draw_tree_trunk(random.randint(50, 175))
        draw_box_tree_leaves()
        tree_height = trunk_height + 50

    retain_original_position(trunk_height)
    return tree_height, trunk_height


def draw_star(max_height):
    """
        Draws a star with line of 10 at every 30 degree from 0 to 360
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """
    ray_length = 10
    turtle.setposition(150, max_height + ray_length + 10)
    turtle.down()
    for angle in range(0, 360, 30):
        turtle.setheading(angle)
        turtle.forward(ray_length)
        turtle.back(ray_length)
    turtle.up()
    turtle.hideturtle()
    pass


def draw_house(wall_height):
    """
        Draws a house of pentagonal shape
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (wall_height,0), heading (east), up
        :return: lumber_available
    """
    lumber_available = 0
    turtle.down()
    turtle.left(90)
    turtle.forward(wall_height)
    lumber_available += wall_height

    turtle.right(45)
    turtle.forward(wall_height / math.sqrt(2))
    lumber_available += (wall_height / math.sqrt(2))
    turtle.right(90)
    turtle.forward(wall_height / math.sqrt(2))
    lumber_available += (wall_height / math.sqrt(2))

    turtle.right(45)
    turtle.forward(wall_height)
    lumber_available += wall_height

    turtle.right(90)
    turtle.forward(wall_height)
    turtle.back(wall_height)
    turtle.setheading(0)
    turtle.up()
    return lumber_available


def calculate_wall_height(lumber_available):
    """
        Calculated wall height with respect to lumber available.
        :return: wall height
    """
    return (math.sqrt(2) * lumber_available) / ((2 * math.sqrt(2)) + 1)


def draw_night_scene():
    """
        Draws trees, house(optional) and a star
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (150, max_height + 20), heading (east), up
        :return: None
    """
    wall_height = 100
    no_of_trees, house_required = get_configurations()
    max_height = 0
    lumber_available = 0
    init()

    if house_required:
        random_house_position = random.randint(1, no_of_trees - 1)
    else:
        random_house_position = -1

    for x in range(0, no_of_trees):
        if x == random_house_position:
            lumber_available += draw_house(wall_height)
            draw_path()

        tree_height, trunk_height = draw_tree()
        if max_height < tree_height:
            max_height = tree_height
        lumber_available += trunk_height

        if x != no_of_trees-1:
            draw_path()

    draw_star(max_height)
    print('Night is done, click on screen to continue...')
    print("We have ", lumber_available," units of lumber for building.")
    wall_height = calculate_wall_height(lumber_available)
    print("We will build a house with walls ", wall_height, " tall.")
    return wall_height


def draw_sun(wall_height):
    """
        Draws a circle
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (100,1.75 * wall_height), heading (east), up
        :return: None
    """
    radius = 30
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(1.75 * wall_height)
    turtle.down()
    turtle.circle(radius)
    turtle.up()
    turtle.hideturtle()
    pass


def bind_day_scene(wall_height):
    def draw_day_scene(x, y):
        """
            Draws house and a sun
            :pre: (relative) pos (0,0), heading (east), up
            :post: (relative) pos (100,1.75 * wall_height), heading (east), up
            :return: None
        """
        turtle.reset()
        turtle.up()
        turtle.setposition(-200, -300)
        draw_house(wall_height)
        draw_sun(wall_height)
        print("Day is done, house is built, press enter to quit.")
        pass
    return draw_day_scene


def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """

    wall_height = draw_night_scene()
    turtle.onscreenclick(bind_day_scene(wall_height))
    turtle.onkeypress(quit, 'Return')
    turtle.listen()
    turtle.setposition(0, 0)
    turtle.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    main()
