from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.color(99, 204, 250)


leo.penup()
leo.goto(0, 0)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()
leo.hideturtle()

bob: Turtle = Turtle()
bob.pencolor("black")
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.speed(90)
i: int = 0
side_length: int = 300
while (i < 300):
    bob.forward(side_length)
    bob.left(105)
    i += 1
    side_length = side_length * 0.97

done()