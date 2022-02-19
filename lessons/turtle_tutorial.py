# from turtle import Turtle, colormode, done
# colormode(255)
# leo: Turtle = Turtle()

# side_length: float = 3

# leo.speed(1000)
# leo.hideturtle()
# leo.penup()
# leo.goto(-60, -200)
# leo.pendown()
# leo.color("black", "pink")

# leo.begin_fill()
# i: int = 0
# while (i < 120):
#     leo.forward(side_length)
#     leo.left(3)
#     i += 1
# leo.end_fill()

# leo.speed(1000)
# leo.hideturtle()
# leo.penup()
# leo.goto(60, -200)
# leo.pendown()
# leo.color("black", "pink")

# leo.begin_fill()
# i: int = 0
# while (i < 120):
#     leo.forward(side_length)
#     leo.left(3)
#     i += 1
# leo.end_fill()

# bob: Turtle = Turtle()
# colormode(255)
# bob.color(0, 0, 0)
# bob.penup()
# bob.goto(-120, -100)
# bob.pendown()
# bob.speed(50)
# counter: int = 0
# while (counter < 150):
#     side_length = side_length * 0.96
#     bob.forward(side_length)
#     bob.left(121)
#     counter += 1

from turtle import Turtle, colormode, done
colormode(255)

background: Turtle = Turtle()
background.speed(500)
background.penup()
background.goto(-500, -500)
background.pendown()
background.begin_fill()
background.color(6, 21, 110)
i: int = 0
while (i < 4):
    background.forward(1000)
    background.left(90)
    i += 1
background.end_fill()


moon: Turtle = Turtle()


moon.pu()
moon.goto(150, 200)
moon.pd()
moon.speed(100)

moon.color("black", "white")
moon.begin_fill()

i: int = 0
while (i < 60):
    moon.forward(3)
    moon.left(3)
    i += 1

moon.setheading(-45)
counter: int = 0
while (counter < 33):
    moon.forward(4)
    moon.left(-3)
    counter += 1

moon.end_fill()

frisbee: Turtle = Turtle()

frisbee.penup()
frisbee.goto(-100, 100)
frisbee.pendown()
frisbee.begin_fill()
frisbee.color("white", "white")
frisbee.setheading(90)
i: int = 0
while (i < 70):
    frisbee.forward(1)
    frisbee.left(2)
    i += 1
frisbee.right(-45)
i = 0
while (i < 70):
    frisbee.forward(1)
    frisbee.left(2)
    i += 1
frisbee.end_fill()

field: Turtle = Turtle()
field.penup()
field.goto(-400, -250)
field.pendown
field.begin_fill()
field.color("brown", "green")
i = 0
while i < 2:
    field.forward(1000)
    field.right(90)
    field.forward(100)
    field.right(90) 
    i += 1

field.end_fill()

lights: Turtle = Turtle()
lights.penup()
lights.goto(-300, -250)
lights.pendown
lights.begin_fill()
lights.color("gray")
lights.left(90)
lights.forward(200)
lights.left(90)
i = 0
while i < 60:
    lights.forward(.5)
    lights.right(3)
    i += 1
lights.forward(25)
i = 0
while i < 60:
    lights.forward(.5)
    lights.right(3)
    i += 1
lights.left(90)
lights.forward(200)
lights.right(90)
lights.forward(20)
lights.end_fill()

player: Turtle = Turtle()

player.penup()
player.goto(-250, -250)
player.pendown()
player.color(241, 156, 107)
player.pensize(10)
player.left(45)
player.forward(20)
player.right(90)
player.forward(20)
player.right(180)
player.forward(20)
player.right(45)
player.forward(30)
player.right(90)
player.forward(10)
player.right(180)
player.forward(20)
player.right(180)
player.forward(10)
player.left(90)
player.forward(10)
player.right(90)
player.begin_fill()
i = 0
while (i < 120):
    player.forward(.25)
    player.left(3)
    i += 1
player.end_fill()

done()


# Yurtle.penup()
# Yurtle.goto(100, 100)
# Yurtle.pendown()
# Yurtle.color("black", "green")
# Yurtle.begin_fill()
# Yurtle.setheading(137.0)
# counter: float = 0
# while counter < 20:
#     i: int = 0
#     while (i < 30 - counter):
#         Yurtle.forward(5)
#         Yurtle.left(3 - (counter / 10))
#         i += 1
#     Yurtle.setheading(270.0)
#     Yurtle.forward(40)
#     Yurtle.left(90)
#     Yurtle.forward(20)
#     Yurtle.left(90)
#     Yurtle.forward(40)
#     Yurtle.setheading(345)
#     counter += 11

# Yurtle.end_fill()


# done()