__author__ = 'asj8139'

"""
Lecture 2.

This is a program which draws word "FONT" using turtle
"""

import turtle

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('FONTT')

def drawF():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (-60,0), heading (east), up
        :return: None
    """
    turtle.left(180)
    turtle.forward(70)
    turtle.forward(25)
    turtle.right(90)
    turtle.down()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.up()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

def main():
    """
    The main function.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :return: None
    """
    init()
    drawF()
    turtle.mainloop()

if __name__ == '__main__':
    main()