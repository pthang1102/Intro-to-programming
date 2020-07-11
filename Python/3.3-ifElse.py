# Draw a square using if-else
import turtle
espoo = turtle.Turtle()
espoo.width(5)

for side in range(4):
    if side == 1:
        espoo.color("blue")
    else:
        espoo.color("yellow")    
    espoo.forward(100)
    espoo.right(90)