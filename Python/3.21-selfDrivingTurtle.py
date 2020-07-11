# This programs draw a 200x200 box. 
# The turtle is running in the box without running out-of-bound.
import turtle
import random

# Function to draw a 200x200 box
def draw_box(length):
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.back(length/2)
    t.left(90)
    t.forward(length/2)
    t.right(90)
    t.pendown()
    for side in range(4):
        t.forward(length)
        t.right(90)
    t.hideturtle()

draw_box(200)

t = turtle.Turtle()
t.shape("turtle")
t.color("olive")
t.penup()
t.speed(1)

for e in range(2000):
    t.right(random.randint(-10, 10))
    t.forward(10)
    
    # Check if the turtle is out-of-bound
    out_of_bounds = t.xcor() < -90 or t.xcor() > 90 or t.ycor() < -90 or t.ycor() > 90

    if out_of_bounds:
        t.right(180)
        t.forward(10)
