# Barbara King Extra Credit htt6_2.py
import turtle

def draw_N_nested_squares(t, side, N):
    for square in range(N):
        t.setpos(-(side/2), -(side/2))
        t.pendown()
        for i in range(4):
            t.lt(90)
        t.penup()            t.fd(side)

        side += 20

def main():
    N = int(input("Enter number of squares to draw: "))
    tess = turtle.Turtle()
    wn = turtle.Screen()
    tess.hideturtle()
    tess.penup()
    tess.pencolor("red")
    wn.bgcolor("light green")
    draw_N_nested_squares(tess, 20, N)
    wn.exitonclick()

if __name__ == "__main__":
    main()