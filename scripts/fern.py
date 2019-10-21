import turtle
from random import random

screen = turtle.Screen()
screen.setup(600,600)
screen.tracer(0)

turtle.speed(0)
turtle.hideturtle()
turtle.color('green')

x,y = (0,0)
scale = 40

for i in range (10000):
    turtle.penup()
    turtle.goto(scale * x, scale * y - 275)
    turtle.pendown()
    turtle.dot(3)
    turtle.update()

    r = random()
    xn,yn = x,y
    if (r <= 0.1):
        x = 0
        y = yn * 0.16
    elif (r <= 0.86):
        x = (xn * 0.85) + (yn * 0.04)
        y = -(xn * 0.04) + (yn * 0.85) + 1.6
    elif (r <= 0.93):
        x = (xn * 0.2) - (yn * 0.26)
        y = (xn * 0.23) + (yn * 0.22) + 1.6
    elif (r <= 1):    
        x = -(xn * 0.15)  + (yn * 0.28) 
        y = (xn * 0.26)  + (yn * 0.24)  + 0.44


screen.exitonclick()
