# This program create a function called 'spiral' with 4 parameters and call it.
import turtle

def spiral(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spiral(100, 45, "cyan", 6)