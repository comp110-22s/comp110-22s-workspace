"""Ex 04--sample turtle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Test
# leo.forward(50)
# leo.left(30)
# leo.right(40)


# Draw square
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# done()

# Simplified
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1
# done()

# Triangle
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
bob: Turtle = Turtle()
bob.color('black')
