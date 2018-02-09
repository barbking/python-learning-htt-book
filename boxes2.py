# Barb King boxes2.py

import turtle
import math
side = 20*math.sqrt(2)
wn = turtle.Screen()
t = turtle.Turtle()
t.up()
t.forward(20)
t.down()
t.left(90)
t.forward(20)
for i in range(3):
    t.left(90)
    t.forward(40)
t.left(90)
t.forward(20)
t.left(45)
t.forward(side)
for i in range(3):
    t.left(90)
    t.forward(side)
wn.exitonclick()