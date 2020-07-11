# This program visualizes the turtle going in a long, straight-line and walking straight off the screen
# Where it turn around and go back the other way
# Using xcor() and ycor()
import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    if t.xcor() < -600 or t.xcor() > 600:
        t.right(180)