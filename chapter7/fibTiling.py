# Barbara King
# fibTiling.py extra credit

import turtle
import random

def fibonacci(N):
    fn_1 = 0
    fn_2 = 1
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        for i in range(1,N):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
    return fn

def draw_square(t, side):
    colors = ["red", "blue", "yellow", "green", "orange"]

    t.fillcolor(colors[random.randint(0,4)])
    t.begin_fill()
    for i in range(6):
        t.forward(side * 10) # multiplying by 10 to make squares bigger for better viewing
        t.right(90)
    t.right(90)
    t.end_fill()

def draw_fibonacci(t, num_squares):
    for num in range(1, num_squares + 1):
        side = fibonacci(num)
        print("in draw_fibonacci func side", side)
        draw_square(t, side)

def main():
    num_squares = int(input("Enter number of Fibonacci squares to draw: "))
    moxie = turtle.Turtle()
    wn = turtle.Screen()
    draw_fibonacci(moxie, num_squares)
    wn.exitonclick()

main()