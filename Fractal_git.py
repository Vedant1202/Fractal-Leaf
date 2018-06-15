
## make leaf fractal using turtle
import turtle
import random

## creating a single leaf
def make_partial_leaf(t, size, angle, c1, c2):
    t.left(angle)
    make_leaf(t, size * c1)

    t.right(angle)
    t.backward(size * c2)

## Recursive function for complete leaf
def make_leaf(t, size):
    if size > 1:
        t.forward(size)
        make_partial_leaf(t, size, 5, 0.8, 0.05)
        make_partial_leaf(t, size, -40, 0.45, 0.2)
        make_partial_leaf(t, size, 35, 0.4, 0.75)

def main():

    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.color("white")
    brad.speed(0)
    brad.hideturtle()

    brad.left(90)
    make_leaf(brad, 60)
    
    window.exitonclick()

main()