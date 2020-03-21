# Turtle Snake Project
# https://www.youtube.com/watch?v=dihj4cpBXkg
import turtle
turtle.setup(width=0.5, height=0.5)
screen = turtle.Screen()
screen.bgcolor("#000000")

t=turtle.Pen()
t.pensize(15)

iro=['yellow', 'blue','red','purple','green']
for i in range (350):
    color=iro[i%len(iro)]
    t.pencolor(color)
    t.forward(i+10)
    t.left(60)
    
turtle.exitonclick()