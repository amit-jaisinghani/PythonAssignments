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

COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'black', 'violet' , 'magenta', 'pink'


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


def draw_polygon(length, sides, status, sum):

    if sides < 3:
        return sum

    angle_of_current_polygon = 180 - (360/sides)

    turtle.color(COLORS[sides-2])


    if status == "fill":
        turtle.begin_fill()
        turtle.pencolor('black')
        turtle.fillcolor(COLORS[sides-2])

    if sides == 3 or sides == 5 or sides == 7:
        for x in range(sides):
            turtle.forward(length)
            sum += length
            sum = draw_polygon(length / 2, sides - 1, status, sum)
            turtle.left(180 - angle_of_current_polygon)

    else:
        for x in range(sides):
            turtle.back(length)
            sum += length
            sum = draw_polygon(length / 2, sides - 1, status, sum)
            turtle.right(180-angle_of_current_polygon)

    if status == 'fill':
        turtle.end_fill()

    return sum


def write_name():
    turtle.up()
    turtle.setpos(-400,-350)
    turtle.down()
    turtle.write("Aditi Shailendra Singhai")
    turtle.up()
    turtle.setpos(-400, -400)
    turtle.down()
    turtle.write("Amit Shyam Jaisinghani")
    turtle.up()
    turtle.setpos(0,0)

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
    sum = 0
    print('Sum: ',draw_polygon(200, sides, status, sum))
    write_name()

    turtle.mainloop()


if __name__ == '__main__':
    main()
