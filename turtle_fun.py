# graph from turtle documentation
# https://docs.python.org/3.5/library/turtle.html

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# Barbara King clockface.py
import turtle
wn = turtle.Screen()
# radi = int(input("Enter radius of your clock, looks best if great than 50: "))
radi = 100
t = turtle.Turtle()
t.color("royal blue")
t.shape("turtle")
t.stamp()
t.penup()
for i in range(12):
    t.forward(radi)
    t.stamp()
    t.setposition(0,0)
    t.left(30)

wn.exitonclick()