# Turtle Snake Project
# URL
import turtle
import random

turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

t = turtle.Pen()
t.pensize(2)
size = screen.screensize()
width = size[0]
height = size[1]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']
t.speed(0)

for i in range(2000):
    x = random.randint(-620, 620)
    y = random.randint(-350, 350)
    color = colors[random.randint(0, len(colors)-1)]
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    r = random.randint(10, 40)
    t.circle(r)
    t.end_fill()

turtle.exitonclick()