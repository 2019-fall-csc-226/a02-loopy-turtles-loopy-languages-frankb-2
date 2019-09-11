######################################################################
# Author: Bryar Frank
# Username: frankb
#
# Assignment: A02: Loopy Turtles
# Purpose: To play around and create loops
######################################################################
# Importing turtle library, creating window, and defining two turtles
import turtle


def draw_shape(t, sz, n_side, m):
    t.rt(21)
    t.fd(m)
    for side in range(n_side):

        t.fd(sz)
        t.rt(360/n_side)


def repeat_shape(polygon):
    size = 10
    move = 10
    increase = 2
    bryar.setheading(0)
    megan.setheading(120)
    gwen.setheading(240)
    for repetitions in range(40):
        draw_shape(bryar, size, polygon, move)
        draw_shape(megan, size, polygon, move)
        draw_shape(gwen, size, polygon, move)
        size = size + 7
        move = move + increase
        increase = increase + .9








num_sides = int(input("How many sides for repeating shapes: "))

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

repeat_shape(num_sides)

wn.exitonclick()