# This program create a function called draw_shape with several parameters.
# Then call it, pass its number of sides, color and side_length as arguments.
# In order to draw a polygon
import turtle

def draw_shape(sides, color, length):
    shape = turtle.Turtle()
    shape.width(5)
    shape.color(color)
    for side in range(sides):
        shape.forward(length)
        shape.right(360 / sides)

draw_shape(15, "darkgreen", 50)