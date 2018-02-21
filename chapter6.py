# Chapter 6 Functions

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawTriangle(t, sz):
    for i in range(2):
        t.forward(sz)
        t.left(120)
    t.forward(sz)

tess = turtle.Turtle()
wn = turtle.Screen()

# drawSquare(tess, 100)
drawTriangle(tess, 100)

wn.exitonclick()