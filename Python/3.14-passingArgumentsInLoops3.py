# This program draws an orb which is made of 12 polygons.
import turtle

def polygon(sides, length):
    t = turtle.Turtle()
    t.color("lime")
    t.speed(8)
    t.width(3)
    angle = 360/sides
    for side in range(sides):
        t.forward(length)
        t.right(angle)
    t.hideturtle()

for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    polygon(n, 35)