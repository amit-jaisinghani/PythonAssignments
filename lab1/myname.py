__author__ = 'asj8139'

"""
Assignment 1: Print last name using turtle.
Author: Amit Shyam Jaisinghani

This is a program which draws word "JAISINGHANI" using turtle in which vowels are printed in Red color and non-vowels character in Black.
"""

import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

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
    turtle.setpos(-400, 0);
    turtle.title('myname')


def drawJ():
    """
        Draws alphabet J.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.forward(MARGIN)
    turtle.down()
    turtle.left(90)
    turtle.forward(15)
    turtle.back(15)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.back(40)
    turtle.up()
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(MARGIN)
    pass


def drawA():
    """
        Draws alphabet A.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.color('red')
    turtle.forward(MARGIN)
    turtle.down()

    side_angle_of_alphabet_A = math.degrees(math.atan(80/25))
    side_of_alphabet_A = math.hypot(80,25)
    upper_angle_of_aplhabet_A = 2 * (180 - 90 - side_angle_of_alphabet_A)
    hypotenuse_side_length_of_upper_triangle = side_of_alphabet_A / 2
    middle_line_of_aplhabet_A = ( hypotenuse_side_length_of_upper_triangle * math.cos( math.radians(side_angle_of_alphabet_A )) ) * 2

    turtle.left(side_angle_of_alphabet_A)
    turtle.forward(side_of_alphabet_A)
    turtle.right(180 - upper_angle_of_aplhabet_A)
    turtle.forward(side_of_alphabet_A / 2)
    turtle.right(180 - side_angle_of_alphabet_A)
    turtle.forward(middle_line_of_aplhabet_A)
    turtle.back(middle_line_of_aplhabet_A)
    turtle.left(180 - side_angle_of_alphabet_A)
    turtle.forward(side_of_alphabet_A / 2)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(MARGIN)
    turtle.color('black')
    pass


def drawI():
    """
        Draws alphabet I.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.color('red')
    turtle.forward(MARGIN)
    turtle.down()
    turtle.forward(50)
    turtle.back(25)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.up()
    turtle.right(90)
    turtle.forward(80)
    turtle.setheading(0)
    turtle.forward(MARGIN)
    turtle.color('black')
    pass


def drawS():
    """
        Draws alphabet S.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.forward(MARGIN)
    turtle.down()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.back(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(80)
    turtle.setheading(0)
    turtle.forward(MARGIN)
    pass


def drawN():
    """
        Draws alphabet N.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.forward(MARGIN)
    turtle.down()
    turtle.left(90)
    turtle.forward(80)

    diagonal_line_of_alphabet_N = math.hypot(80,50)
    angle_of_alphabet_N = math.degrees(math.acos(80/diagonal_line_of_alphabet_N))

    turtle.right(180 - angle_of_alphabet_N)
    turtle.forward(97)
    turtle.left(180 - angle_of_alphabet_N)
    turtle.forward(80)
    turtle.back(80)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(MARGIN)
    pass


def drawG():
    """
        Draws alphabet G.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.forward(MARGIN)
    turtle.setheading(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.down()
    turtle.back(50)
    turtle.left(90)
    turtle.back(80)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(15)
    turtle.back(15)
    turtle.left(90)
    turtle.forward(40)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(MARGIN)
    pass


def drawH():
    """
        Draws alphabet H.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (70,0), heading (east), up
        :return: None
    """
    turtle.forward(MARGIN)
    turtle.down()
    turtle.left(90)
    turtle.forward(80)
    turtle.back(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(40)
    turtle.back(80)
    turtle.up()
    turtle.setheading(0)
    turtle.forward(MARGIN)
    pass

def drawMyFamilyName():
    """
            The main function.
            :pre: (relative) pos (0,0), heading (east), up
            :post: (relative) pos (840,0), heading (east), up
            :return: None
        """
    drawJ()
    drawA()
    drawI()
    drawS()
    drawI()
    drawN()
    drawG()
    drawH()
    drawA()
    drawN()
    drawI()
    pass

def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (840,0), heading (east), up
        :return: None
    """
    init()
    drawMyFamilyName()
    turtle.mainloop()


if __name__ == '__main__':
    main()
