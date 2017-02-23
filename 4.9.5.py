from turtle import*
bgcolor("green")
color("blue")
speed(-1)
pensize(2)

n=100
length=5

for i in range(n):
    forward(length*(i+1))
    right(89)
