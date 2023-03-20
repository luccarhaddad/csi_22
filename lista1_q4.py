import turtle
import numpy as np

def draw_spirals(t, n):
    t.up()
    t.setpos(x=-100, y=0)
    t.down()
    for i in range(n):
        t.forward(i+2)
        t.right(90)
    t.up()
    t.setpos(x=100, y=0)
    t.down()
    for i in range(n):
        t.forward(i+2)
        t.right(91)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Spiral Drawing")
alex = turtle.Turtle()

draw_spirals(alex, 100)