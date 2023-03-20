import turtle
import numpy as np


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Square drawing")
alex = turtle.Turtle()

def draw_poly(t, n, sz):
    t.up()
    t.setpos(x=-sz/2,y=-sz/(2*np.tan(np.pi/n)))
    t.down()
    for i in range(n):
        t.width(4)
        t.color('purple')
        t.forward(sz)
        t.left(360/n)

draw_poly(alex, 8, 50)

wn.mainloop()