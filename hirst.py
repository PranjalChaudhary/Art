import turtle as t
from random import choice
from turtle import Turtle, Screen

import colorgram

t.colormode(255)
timmy = Turtle()

colors = colorgram.extract('download.jpg', 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))
color_list.pop(1)
color_list.pop(0)
color_list.pop(2)
screen = Screen()
screen.bgcolor(color_list.pop(1))


def random_color():
    return choice(color_list)


timmy.penup()
timmy.setpos(-725, -365)
Initial_x = timmy.xcor()
Initial_y = timmy.ycor()


def hirst(initial_x, initial_y, rows):
    for i in range(rows):
        timmy.setposition((initial_x, initial_y + 25 * i))
        for j in range(rows):
            timmy.dot(11, choice(color_list))
            timmy.forward(25)


hirst(Initial_x, Initial_y, 59)

screen.screensize(300, 300)
screen.exitonclick()
