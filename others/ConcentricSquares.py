

import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# global constant for left and right margin of an alphabet
MARGIN = 10


def init():
    """
    Initialize for drawing.  (-400, -400) is in the lower left and
    (400, 400) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    turtle.up()
    turtle.setheading(0)
    turtle.title('squares')
    pass


def drawSquare():
    turtle.setheading(0)
    turtle.down()
    for x in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.left(60)
    turtle.forward(50)
    turtle.up()
    pass


def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
    """
    init()
    drawSquare()
    drawSquare()
    turtle.mainloop()


if __name__ == '__main__':
    main()