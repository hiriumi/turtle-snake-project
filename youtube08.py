# Turtle Snake Project
# https://www.youtube.com/watch?v=NVc3AbjI_2c

import turtle
    
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

t = turtle.Pen()

iro=['limegreen','tomato', 'royalblue', 'gold']

t.speed(10)

for i in range (300):
    t.pensize(7)
    color=iro[i%4]
    t.pencolor(color)
    t.down()
    t.forward(10+i)
    t.forward(10+i)
    t.up()
    t.left(91)
    t.forward(4+i)
    t.right(30)

turtle.exitonclick()