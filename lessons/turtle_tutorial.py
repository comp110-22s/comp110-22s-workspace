from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(20)
leo.hideturtle()

leo.penup()
leo.goto(-250, -175)
leo.pendown()

leo.pencolor(99, 204, 250)
leo.fillcolor(255, 0, 0)

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(500)
    leo.left(120)
    i += 1
leo.end_fill()


bob: Turtle = Turtle()

bob.penup()
bob.goto(-250, -175)
bob.pendown()
bob.pencolor(0, 0, 0)

bob.speed(75)
side_length: float = 500.0

h: int = 0
while h < 200:
    bob.forward(side_length)
    bob.left(121)
    h += 1
    side_length = side_length * 0.97
done()