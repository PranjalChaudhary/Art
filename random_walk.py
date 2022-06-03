import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
angles = [timmy.right, timmy.left]
angle_values = [0, 90, 180, 270]
timmy.width(10)
timmy.speed("fastest")
for i in range(5000):
    timmy.pencolor(random_color())
    timmy.forward(35)
    choice(angles)(choice(angle_values))


screen = Screen()
screen.screensize(300,300)
screen.exitonclick()
