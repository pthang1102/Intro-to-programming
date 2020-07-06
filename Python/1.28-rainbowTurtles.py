# This program draw rainbow-colors shapes using Turtle module

import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
line = turtle.Turtle()
line.width(5)

# Move back without drawing anything, then it is easier to observe
line.penup()
line.back(150)
line.pendown()

# DRAW A RAINBOW HEXAGON
#for color in rainbow:
#    line.color(color)
#    line.forward(100)
#    line.right(60)

#DRAW 6 STARS WITH DIFFERENT COLORS
for color in rainbow:
    line.color(color)
    for side in [1, 2, 3, 4, 5]:
        line.forward(50)
        line.right(144)
    line.penup()
    line.right(60)
    line.forward(50)
    line.pendown()