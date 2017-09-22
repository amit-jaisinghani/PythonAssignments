import sys

__author__ = 'asj8139,ass7436'

"""
Assignment 3: Polygons
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai


"""

import turtle

# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 8

COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'black', 'violet'


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
    turtle.setpos(0, 0)
    turtle.down()
    turtle.title('Polygons')


def take_input_from_the_user():
    if len(sys.argv) != 3:
        print("Usage: You need to enter sides_of_polygon and fill|unfill. ")
        sys.exit(1)

    sides = int(sys.argv[1])
    print(sides)

    status = (sys.argv[2])
    print(status)
    return sides, status


def draw_polygon(length, sides, status, turtle):

    if sides < 3:
        return

    angle_of_current_polygon = 180 - (360/sides)

    if status == "fill":
        print(COLORS[sides])
        turtle.color(COLORS[sides])
        turtle.begin_fill()

    if sides == 3 or sides == 5 or sides == 7:
        for x in range(sides):
            turtle.forward(length)
            draw_polygon(length / 2, sides - 1, status, turtle)
            turtle.left(180 - angle_of_current_polygon)

    else:
        for x in range(sides):
            turtle.back(length)
            draw_polygon(length / 2, sides - 1, status, turtle)
            turtle.right(180-angle_of_current_polygon)

    turtle.end_fill()

    pass


def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """
    sides, status = take_input_from_the_user()
    init()
    # turtle.tracer(0, 0)
    draw_polygon(200, sides, status, turtle)

    turtle.mainloop()


if __name__ == '__main__':
    main()
