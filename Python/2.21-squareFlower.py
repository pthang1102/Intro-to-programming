# This program draws a flower out of squares
import turtle

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

art = turtle.Turtle()
art.width(5)
art.color("violet")
art.speed(10)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(art)