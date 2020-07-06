# This program draw a three-color lines with spaces between them.

import turtle

line = turtle.Turtle()
line.width(5)

# Move back without drawing anything, then it is easier to observe
line.penup()
line.back(150)
line.pendown()

for color in ["red", "orange", "yellow"]:
    line.color(color)
    line.forward(50)
    line.penup()
    line.forward(50)
    line.pendown()