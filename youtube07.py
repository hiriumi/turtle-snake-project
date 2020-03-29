# Turtle Snake Project
# URL
import turtle
import random
import math

def draw_regular_polygon(corners, t):
    if corners < 3:
        raise Exception("corners value must be larger than 2.")
    
    num = corners - 2
    angle = num*180/corners

    for i in range(1, corners+1):
        t.forward(50)
        t.right(angle+180)

    
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

t = turtle.Pen()
t.pensize(2)
t.pencolor('white')
t.left(90)
t.speed(0)

for i in range(3, 40):
    draw_regular_polygon(i, t)

t.right(90)

for i in range(3, 40):
    draw_regular_polygon(i, t)

t.right(90)

for i in range(3, 40):
    draw_regular_polygon(i, t)

t.right(90)

for i in range(3, 40):
    draw_regular_polygon(i, t)    

turtle.exitonclick()