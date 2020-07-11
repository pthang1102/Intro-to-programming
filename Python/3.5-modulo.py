# This program draws a staircase using % modulo
import turtle

step = turtle.Turtle()
step.width(5)
step.color("green")

def draw_staircase():
    for n in range(19):
        step.forward(20)
        if n%2 == 0:
            step.left(90)
        else:
            step.right(90)    

draw_staircase()