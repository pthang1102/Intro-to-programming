# This program draws 2 star-cluster by passing arguments in loops.
import turtle

def star(color, sides, length, angle, distance):
    draw = turtle.Turtle()
    draw.color(color) # colorful!
    draw.width(5) # visible!
    draw.speed(8) # fast!
    draw.penup()
    draw.left(angle) # away from center
    draw.forward(distance)
    draw.pendown() # start drawing!
    for side in range(sides):
        draw.forward(length)
        draw.left(720 / sides)
    draw.hideturtle() # just the star

# Big pink star-cluster
for angle in [180, 135, 90, 45, 0]:
    star("pink", 5, 50, angle, 100)

# Small red star-cluster
for angle in [180, 135, 90, 45, 0]:
    star("red", 5, 30, angle, 60)
