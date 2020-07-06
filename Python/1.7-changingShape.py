# This program draw a red pentagon with turtle library
import turtle

thang = turtle.Turtle()
thang.color("red")

for side in [1, 2, 3, 4, 5]:
    thang.forward(100)
    thang.right(72)