# import turtle               # allows us to use the turtles library
# wn = turtle.Screen()        # creates a graphics window
# alex = turtle.Turtle()      # create a turtle named alex
# alex.forward(150)           # tell alex to move forward by 150 units
# alex.left(90)               # turn by 90 degrees
# alex.forward(75)            # complete the second side of a rectangle
# alex.left(90)
# alex.forward(150)
# alex.left(90)
# alex.forward(75)

import turtle

wn = turtle.Screen()
color = input("Enter a background color")
wn.bgcolor(color)        # set the window background color

turtle_color = input("Enter a turtle color")
turtle_pen = int(input("Enter a pen size"))
tess = turtle.Turtle()
tess.color(turtle_color)              # make tess blue
tess.pensize(turtle_pen)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas