# This program draws a 12-sided dodecagon that has 3-colors patterns
import turtle

t = turtle.Turtle()
t.width(5)

for n in range(12):
    if n%3 == 0:
        t.color("red")
    elif n%3 == 1:
        t.color("green")
    else:
        t.color("purple")
    t.forward(50)
    t.right(360/12)
