"""Drawing Triangles with Turtles."""

__author__ = 730486473

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.color("Green", "Pink")

leo.begin_fill()

leo.penup()
leo.goto(-150, -120)
leo.pendown()

i: int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

# BOBS TURN

bob: Turtle = Turtle()

bob.speed(10000000000)
bob.hideturtle()

bob.pencolor("pink")
bob.color("black")

bob.penup()
bob.goto(-150, -120)
bob.pendown()

side_length: float = 300

i: int = 0
decrease: float = 0.98
angle: int = 121
while(i < 1000):
    bob.forward(side_length)
    bob.left(angle)
    side_length *= decrease
    i += 1

done()