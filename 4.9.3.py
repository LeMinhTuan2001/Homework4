import turtle
from turtle import*
bgcolor("green")

tess=turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")

def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

draw_poly(tess,8,50)
