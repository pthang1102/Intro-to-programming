# This program draws a green hexagon-chain (8 pieces of chain) using Turtle module
import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

line = turtle.Turtle()
line.color("green")
line.width(5)

# Move back so that the chain is in the center.
line.penup()
line.back(80)
line.pendown()

for link in links:
    # Draw a hexagon
    for side in sides:
        line.forward(10)
        #Try to draw another pattern
        #line.forward(50)
        line.right(60)
    
    # Move over to the next link
    line.penup()
    line.forward(20)
    # Try to draw another pattern
    #line.left(60)
    line.pendown()

line.hideturtle()
    