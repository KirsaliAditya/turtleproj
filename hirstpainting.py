import turtle
import colorgram
import random

turtle.colormode(255)
addy = turtle.Turtle()
addy.speed("fastest")
addy.hideturtle()


def extract_colour():
    color_list = []
    colours = colorgram.extract("h1.jpg", 38)
    for color in colours:
        color_list.append((color.rgb.r, color.rgb.b, color.rgb.g))
    return color_list


def painting(colour):
    for i in range(1, 101):
        addy.dot(15, random.choice(colour))
        addy.penup()
        addy.forward(50)
        addy.pendown()
        if i % 10 == 0:
            addy.setheading(90)
            addy.penup()
            addy.forward(50)
            addy.setheading(180)
            addy.forward(500)
            addy.setheading(0)
            addy.pendown()


def initial_setup():
    addy.up()
    addy.setheading(-90)
    addy.forward(225)
    addy.setheading(0)
    addy.back(220)
    addy.down()


colour_list = extract_colour()
initial_setup()
painting(colour_list)
screen = turtle.Screen()
screen.exitonclick()
