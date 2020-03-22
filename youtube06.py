# Turtle Snake Project
# https://www.youtube.com/watch?v=RPqJzABd-8g
import turtle
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

n=turtle.Pen()

n.right(90)
n.pensize(20)
iro=['orchid', 'dark slate blue','blueviolet','mediumvioletred','hotpink','lightpink','darkviolet','dark slate blue','lavenderblush']
n.speed(10)
r=160
for i in range (250):
    color=iro[i%9]
    n.pencolor(color)
    n.circle(r)
    r=r-0.7
    n.right(40)
    n.forward(50)
    n.circle(1-i*1.4)

turtle.exitonclick()