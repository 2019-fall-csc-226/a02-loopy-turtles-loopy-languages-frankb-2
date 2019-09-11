######################################################################
# Author: Bryar Frank
# Username: frankb
#
# Assignment: A02: Loopy Turtles
# Purpose: To play around and create loops
######################################################################
# Importing turtle library, creating window, and defining two turtles
import turtle


######################################################################
# define functions for drawing a polygon and repeating the polygon
######################################################################

def draw_shape(t, sz, n_side, m):
    """
    Draws a polygon and resets position of turtle
    """
    t.rt(21)
    t.fd(m)
    for side in range(n_side):
        t.fd(sz)
        t.rt(360/n_side)


def repeat_shape(polygon):
    """
    Takes the polygon and repeats it in a spiraling pattern
    :param polygon:
    :return:
    """
    size = 10
    move = 10
    increase = 2
    bryar.setheading(0)
    megan.setheading(120)
    gwen.setheading(240)
    for repetitions in range(30):
        draw_shape(bryar, size, polygon, move)
        draw_shape(megan, size, polygon, move)
        draw_shape(gwen, size, polygon, move)
        size = size + 7
        move = move + increase
        increase = increase + .9


######################################################################
# Ask User how many sides for polygon and save for the functions
######################################################################
num_sides = int(input("How many sides for repeating shapes: "))


######################################################################
# Create Screen, Turtles, and Settings for Each
######################################################################
wn = turtle.Screen()
wn.setup(width=1366, height=768, startx=0, starty=0)
wn.bgcolor('black')

bryar = turtle.Turtle()
megan = turtle.Turtle()
gwen = turtle.Turtle()

bryar.color('Cyan')
gwen.color("Deep Sky Blue")
megan.color("Firebrick")

bryar.speed(0)
gwen.speed(0)
megan.speed(0)

bryar.pensize(10)
gwen.pensize(10)
megan.pensize(10)

######################################################################
# Fire that baby off!!!
######################################################################
repeat_shape(num_sides)

wn.exitonclick()