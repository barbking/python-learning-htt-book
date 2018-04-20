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

def drawStar(t, sz):
    angle = ((8-2)*180)/8
    for i in range(8):
        t.forward(sz)
        t.left(angle)

def drawOctagon(t, sz):
    for i in range(8):
        t.forward(sz)
        t.left(45)

def drawPolygon(t, sideLength, numSides):
    angle = 360/numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.left(angle)

def drawCircle(t, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(t, sideLength, 360)


tess = turtle.Turtle()
wn = turtle.Screen()

# drawSquare(tess, 100)
# drawTriangle(tess, 100)
# drawStar(tess, 50)
# drawOctagon(tess, 50)
# drawPolygon(tess, 50, 5)
drawCircle(tess, 100)
wn.exitonclick()
