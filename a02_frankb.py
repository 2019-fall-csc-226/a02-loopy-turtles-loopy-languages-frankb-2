######################################################################
# Author: Bryar Frank
# Username: frankb
#
# Assignment: A02: Loopy Turtles
# Purpose: To play around and create loops
######################################################################
# Importing turtle library, creating window, and defining two turtles
import turtle


def draw_shape(t, sz, n_side):

    for side in range(n_side):
        t.fd(sz)
        t.rt(360/n_side)

def repeat_shape(polygon):

    size = 10
    for repetitions in range(10):
        draw_shape(turtle, size, polygon)
        size



num_sides = int(input("How many sides for repeating shapes: "))

bryar = turtle.Turtle()
#megan = turtle.Turtle()
#gwen = turtle.Turtle()
bryar.color('Cyan')
#gwen.color("Deep Sky Blue")
#megan.color("Firebrick")
wn = turtle.Screen()
wn.setup(width=1366, height=768, startx=0, starty=0)
wn.bgcolor('black')

repeat_shape(num_sides)

wn.exitonclick()
