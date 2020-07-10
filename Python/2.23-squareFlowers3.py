# This program draws 2 different-color flowers using 2 turtle objects.
import turtle

helsinki = turtle.Turtle()
helsinki.color("darkblue")
helsinki.width(5)
helsinki.speed(10)

espoo = turtle.Turtle()
espoo.color("pink")
#espoo.width(5)
espoo.speed(10)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(helsinki)
draw_flower(espoo)