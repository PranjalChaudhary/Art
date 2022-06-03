import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
angles = [timmy.right, timmy.left]
angle_values = [0, 90, 180, 270]
# timmy.width()
timmy.speed("fastest")


def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(75)
        timmy.setheading(timmy.heading() + size_of_gap)


spirograph(10)
screen = Screen()
screen.screensize(300, 300)
screen.exitonclick()
