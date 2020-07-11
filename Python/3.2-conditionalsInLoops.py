# This programs draw a square with 2 yellow sides and 2 blue sides by using Conditional inside loop.
import turtle
espoo = turtle.Turtle()
espoo.width(5)

for side in range(4):
    if side == 0:
        espoo.color("blue")
    if side == 2:
        espoo.color("yellow")
    espoo.forward(100)
    espoo.right(90)    