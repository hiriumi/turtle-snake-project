# Turtle Snake Project
# YouTube URL here.
import turtle
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

loop_count = 200
angle=121
t=turtle.Pen()
t.speed(10)

r=0
g=0
b=0

t.pensize(15)
for i in range(loop_count):
    r=r+2
    if r >= 255:
        r = 255

    if r == 255:
        g=g+2
        if g >= 255:
            g = 255
    
    t.pencolor(r/255.0, g/255.0, b/255.0)
    t.circle(10+i)
    t.left(angle)

turtle.exitonclick()