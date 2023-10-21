import turtle
import random


def colour_sel():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


turtle.colormode(255)
addy_turtle = turtle.Turtle()

addy_turtle.speed("fastest")
size = int(360 / 10) + 1
addy_turtle.width(2)
for side in range(size):
    heading = addy_turtle.heading()
    addy_turtle.color(colour_sel())
    addy_turtle.circle(150)
    addy_turtle.setheading(heading + 10)

screen = turtle.Screen()
screen.exitonclick()
