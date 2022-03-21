"""EX04: a turtle program tutorial + mini-project."""

__author__: str = "730466987"

# How to import functions:
from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

# How to make the Turtle follow any commands:
# (see example movements below)

# leo.forward(50)
# leo.left(30)
# leo.right(40)

# Here's how to draw a square with the Turtle!

# leo.forward(100)
# leo.left(90)
# leo.forward(100)
# leo.left(90)
# leo.forward(100)
# leo.left(90)
# leo.forward(100)
# leo.left(90)

# To avoid the above example when trying to draw a square, use the below simplification:

# i: int = 0
# while (i < 4):
#   leo.forward(100)
#   leo.left(90)
#   i = i + 1

# Here's how to draw a triangle:

# i: int = 0
# while (i < 3):

#   leo.forward(100)
#   leo.left(120)
#   i = i + 1

# How to make the drawing in a different part of the screen AND how to move the turtle without having it draw:
# How to change the color of the pen + a fill color:

# leo.color(255, 58, 241)
# or
leo.pencolor(27, 128, 8)
leo.fillcolor(197, 25, 245)

# How to control the speed and visibility of the turtle:
leo.speed(50)
leo.hideturtle()

leo.begin_fill()
leo.penup()
leo.goto(-90, -50)
leo.pendown()

i: int = 0
while (i < 3):
    leo.forward(200)
    leo.left(120)
    i = i + 1

leo.end_fill()

# Drawing another triangle:

bob: Turtle = Turtle()

bob.pencolor(116, 14, 145)
bob.speed(75)
bob.penup()

bob.goto(-90, -50)

bob.pendown()

ib: int = 0
side_length: float = 200

while (ib < 150):
    bob.forward(side_length)
    bob.left(122.5)
    side_length = side_length * 0.97
    ib = ib + 1

done()