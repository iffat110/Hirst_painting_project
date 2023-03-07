import turtle
from turtle import Turtle, Screen
import random
from typing import Tuple

tim = Turtle()
turtle.colormode(255)
screen = Screen()
num_of_dots = 100
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()


def follow():
    for dot_counts in range(1, num_of_dots + 1):
        tim.dot(20, random_color())
        tim.penup()
        tim.forward(50)
        tim.pendown()

        if dot_counts % 10 == 0:
            tim.penup()
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


follow()

screen.exitonclick()
