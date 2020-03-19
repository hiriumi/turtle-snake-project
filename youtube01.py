# This file was used for YouTube video at 
# https://www.youtube.com/watch?v=2mr1tsOxkUw
import turtle

t=turtle.Pen()
t.pensize(15)

iro=['red', 'orange', 'green']

for i in range (500):
    color=iro[i%3]
    t.pencolor(color)
    t.forward(i+10)
    t.left(71)
    
turtle.exitonclick()