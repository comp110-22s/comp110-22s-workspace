import turtle as t
import random

def tree(x: float, y: float) -> None:
    """Paint a beautiful tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK_LENGTH = 100.0
    ANGLE = 90.0
    branch(TRUNK_LENGTH, ANGLE)


def branch(length: float, angle: float) -> None:
    """Paint a beautiful branch...recursively!"""
    t.setheading(angle)
    t.forward(length)
    t.update()
    
    if length < 3.0:
        ...
    else:
        nature: float = random() * 20.0
        branch(length * .75, angle + 5.0 + nature)
        branch(length * .70, angle - (5 + nature))
    t.setheading(angle + 180.0)
    t.forward(length)


t.speed(0)
tree(0, 0)
t.getscreen().onclick(tree)
t.done()