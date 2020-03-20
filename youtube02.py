# This file was used for Fireworks Shuriken YouTube video
# https://www.youtube.com/watch?v=BJCSOd5f7mI

import turtle

turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

screen.setup(width=0.555, height=0.555, startx=100, starty=100)
width, height = screen.window_width(), screen.window_height()
canvas = screen.getcanvas()

left, top = 400, 400
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)


t=turtle.Pen()
t.pensize(11)

speed = 1
for i in range(1, 200):
    speed = speed + 0.1
    t.speed(speed)
    t.pencolor('blue')
    t.forward(100)
    t.pencolor('purple')
    t.forward(50)
    t.pencolor('red')
    t.right(159)
    t.pencolor('yellow')
    t.forward(i)
    t.pencolor('orange')
    t.left(9)
    t.forward(30)
    t.pencolor('green')
    t.circle(30)
    t.left(90)
    t.pencolor('black')
    t.forward(20)

turtle.exitonclick()