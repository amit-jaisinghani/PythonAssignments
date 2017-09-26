import sys

__author__ = 'asj8139,ass7436'

"""
Assignment 3: Polygons
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program draws polygons of decreasing sides, recursively until the shape is a triangle. It also calculates sum of 
all sides of the polygons drawn.

"""

import turtle

# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

SIDE_LENGTH = 200

FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 4

COLORS = 'purple','grey','pink','#f9e611', '#f9104a', 'orange', 'green', '#990109', '#d8c9ca'


def init():
    """
        Initialize for drawing.  (-400, -400) is in the lower left and
        (400, 400) is in the upper right.
        :pre: pos (0,0), heading (east), up
        :post: pos (-100,-200), heading (east), down
        :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    turtle.up()
    turtle.setheading(0)
    turtle.setpos(-100,-200)
    turtle.down()
    turtle.title('Polygons')


def take_input_from_the_user():
    """
        Reads number of sides and status for drawing polygon from command line argument. If empty, program exits.
        :return: number of sides, status - fill, unfill
    """
    if len(sys.argv) != 3:
        print("Usage: You need to run program in format given below : ")
        print("$ python3 polygons.py #_sides [fill|unfill]")
        sys.exit(1)

    sides = int(sys.argv[1])
    if 3>sides or sides>8 :
        print("Usage: the value of side should be between 3 and 8.")
        sys.exit(1)

    status = (sys.argv[2])
    if status != 'fill' and status != 'unfill':
        print("Usage: enter valid status [fill | unfill].")
        sys.exit(1)

    return sides, status


def draw_polygon(length, sides, status):
    """
        Recursively draws polygons on the vertices of main figure drawn at the heading of the vertices until the shape
        is a triangle
        :pre: pos (0,0), heading (start_heading), up
        :post: pos (0,0), heading (start_heading), down
        :return: sum of length of all sides of polygon
    """
    vertices, headings, sum = draw_figure(length, sides, status)

    if sides == 3:
        return sum

    sides = sides - 1
    for x in range(len(headings)):
        turtle.setposition(vertices[x][0], vertices[x][1])
        turtle.setheading(headings[x])
        sum += draw_polygon(length/2, sides, status)

    return sum


def draw_figure(length, sides, status):
    """
        Draws polygon of sides and length specified in arguments and fills polygon with color based on value of status
        :pre: pos (0,0), heading (start_heading), up
        :post: pos (0,0), heading (start_heading), down
        :return: vertices of polygon, headings of the vertices, sum of length of all sides of polygon
    """
    sum = 0
    vertices = []
    headings = []
    offset = 0;
    turtle.down()
    if status == "fill":
        turtle.pensize(FILL_PEN_WIDTH)
        turtle.fillcolor(COLORS[sides]
)
        turtle.begin_fill()
        offset = 180
    elif status == "unfill":
        turtle.pensize(UNFILL_PEN_WIDTH)
        turtle.pencolor(COLORS[sides]
)
        offset = 180

    angle = (360 / sides)

    for x in range(sides):
        vertices.append(turtle.position())
        headings.append(turtle.heading() + offset)
        turtle.forward(length)
        sum += length
        turtle.left(angle)

    if status == "fill":
        turtle.end_fill()

    turtle.up()
    return vertices, headings, sum


def write_name():
    """
        Writes authors name using turtle.write() function.
        :pre: pos (0,0), heading (start_heading), up
        :post: pos (0,0), heading (start_heading), down
        :return: None
    """
    turtle.color('black')
    turtle.up()
    turtle.setpos(600,350)
    turtle.down()
    turtle.write("Aditi Shailendra Singhai")
    turtle.up()
    turtle.setpos(600, 400)
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
    turtle.tracer(0, 0)
    print('Sum: ',draw_polygon(SIDE_LENGTH, sides, status))
    write_name()
    turtle.ht()
    turtle.update()
    turtle.mainloop()


if __name__ == '__main__':
    main()
