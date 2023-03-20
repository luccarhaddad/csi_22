import turtle
import numpy as np

def drawSquare(t, sz):
    t.up()
    t.setpos(x=-sz/2, y=-sz/2)
    t.down()
    for i in range(4):
        t.width(4)
        t.color('purple')
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Square drawing")
alex = turtle.Turtle()

for j in range(5):
    drawSquare(alex, 20 + 20*j)

def sum_to(n):
    return (1+n)*(n/2)
