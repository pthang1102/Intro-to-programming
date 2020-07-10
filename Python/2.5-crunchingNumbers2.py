# This program draws a 20-sided spirangle
import turtle
t = turtle.Turtle()
t.color("darkblue")
t.width(5)

for side in range(20):
    t.forward(10*side)
    t.right(120)