# This program draws a triangle boogie by defining Function called triangle_patterns
import turtle

def triangle_patterns(color, start_angle):
    p = turtle.Turtle()
    p.color(color)
    p.width(5)
    p.right(start_angle)
    for shape in range(6):
        for side in range(3):
            p.forward(100)
            p.right(120)
        p.right(15)
    p.hideturtle()

triangle_patterns("red", 0)
triangle_patterns("blue", 120)
triangle_patterns("green", 240)