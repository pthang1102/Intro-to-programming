# This function draw a hundred-sided polygon by using Function 'range' and Turtle module
import turtle

sides = range(100)
t = turtle.Turtle()
t.color("red")
t.width(5)

for side in sides:
    t.forward(5)
    t.right(360 / 100)