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