# Turtle Snake Project
# https://youtu.be/wFwfFcu5GVw
import turtle

def draw(speed):
    t=turtle.Pen()
    t.speed(speed)
    t.pensize(15)

    iro=['yellow', 'blue','red','purple','green']
    for i in range (350):
        color=iro[i%5]
        t.pencolor(color)
        t.circle(i+10)
        t.left(60)

turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

draw(10)
turtle.resetscreen()
draw(0)

turtle.exitonclick()