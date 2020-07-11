# This program draws an interesting pattern using Random
import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t = turtle.Turtle()
t.width(20)

for step in range(100): 
    angle = random.randint(-90, 90) # Use a random angle
    color = random.choice(colors) # Use a random color

    t.color(color)
    t.right(angle)
    t.forward(10)