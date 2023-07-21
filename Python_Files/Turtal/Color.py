import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
screen = Screen()
tim.speed("fastest")
color_list = [(202, 164, 164), (240, 245, 245), (236, 239, 239), (149, 75, 75), (222, 201, 201),
              (53, 93, 93), (170, 154, 154), (138, 31, 31), (134, 163, 163), (197, 92, 92),
              (47, 121, 121), (73, 43, 43), (145, 178, 178), (14, 98, 98), (232, 176, 176),
              (160, 142, 142), (54, 45, 45), (101, 75, 75), (183, 205, 205), (36, 60, 60),
              (19, 86, 86), (82, 148, 148), (147, 17, 17), (27, 68, 68), (12, 70, 70),
              (107, 127, 127), (176, 192, 192), (168, 99, 99)]
tim.pu()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)


def move():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)


def turn_left():
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(50)
    move()


def turn_right():
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(0)
    tim.fd(50)
    move()


move()
turn_left()
turn_right()
turn_left()
turn_right()
turn_left()
turn_right()
turn_left()
turn_right()
turn_left()

screen.exitonclick()
