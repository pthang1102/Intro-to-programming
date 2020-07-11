# This program draws beads with red-green-blue colors.
import turtle

def bead_color(num):
    if num%3 == 0:
        return "red"
    if num%3 == 1:
        return "green"
    if num%3 == 2:
        return "blue"

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
#t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

for n in range(10):
    t.color(bead_color(n))
    bead(t)
    t.forward(40)