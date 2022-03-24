"""Sunset Over the Ocean. Now With Sharks!"""

__author__ = "730474722"

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    square(0.0, 0.0, "#7B98EB")
    square(-355.0, 0.0, "#7B98EB")
    square(-355.0, -355.0, "#2660FF")
    square(0.0, -355.0, "#2660FF")
    semi_circle(160.0, 0.0)
    scribble_waves(-170.0, 0.0)
    i: int = 0
    while i < 100:
        stars(randint(-350, 350), randint(120, 350), randint(1, 10))
        i += 1
    sharks(300.0, -100.0, 35)
    sharks(310.0, -160.0, 30)
    sharks(260.0, -130.0, 40)
    done()
    return


def scribble_waves(x: float, y: float) -> None:
    """A reflection of the sunset."""
    wavy: Turtle = Turtle()
    wavy.speed(30)
    wavy.color(247, 244, 131)
    j: int = 0
    wavy.penup()
    wavy.goto(x, y) 
    wavy.pendown()
    up = 320
    zigzag: int = 178
    while j < 13:
        wavy.forward(up)
        wavy.right(zigzag)
        up *= .9
        wavy.forward(up)
        wavy.left(zigzag)
        up *= .9
        j += 1
    wavy.hideturtle()
    return


def square(x: float, y: float, color: str) -> None:
    """Draws a square given the coordinates and color."""
    block: Turtle = Turtle()
    block.speed(30)
    block.goto(x, y)
    block.color(f"{color}")
    block.begin_fill()
    i: int = 0
    side: int = 355
    while i < 4:
        block.forward(side)
        block.left(90)
        i += 1
    block.end_fill()
    block.hideturtle()
    return


def semi_circle(x: float, y: float) -> None:
    """Draws a semi-circle to the left starting from x, y."""
    semi: Turtle = Turtle()
    semi.speed(10)
    semi.goto(x, y)
    semi.pencolor("black")
    semi.fillcolor("yellow")
    semi.setheading(136)
    semi.pendown()
    semi.begin_fill()
    i: int = 5
    up: int = 40
    while i < 15:
        semi.left(i)
        semi.forward(up)
        i += 1
    semi.goto(x, y)
    semi.end_fill()
    semi.hideturtle()
    return
    

def stars(x: float, y: float, size: int) -> None:
    """Stars for the night sky."""
    star: Turtle = Turtle()
    star.speed(200)
    star.pencolor("#FBFF75")
    star.fillcolor("#D5D5D5")
    j: int = 0
    star.penup()
    star.goto(x, y) 
    star.right(90)
    star.pendown()
    star.begin_fill()
    while j < 4:
        star.forward(size)
        star.right(135)
        star.forward(size)
        star.left(45)
        j += 1
    star.end_fill()
    star.hideturtle()
    return


def sharks(x: float, y: float, size: int) -> None:
    """Draws 'sharks' to liven up the water."""
    jaws: Turtle = Turtle()
    jaws.penup()
    jaws.goto(x, y)
    jaws.pendown()
    jaws.pencolor("black")
    jaws.fillcolor("silver")
    jaws.begin_fill()
    jaws.forward(size)
    jaws.left(130)
    jaws.forward(size)
    jaws.goto(x, y)
    jaws.end_fill()
    jaws.hideturtle()
    return


if __name__ == "__main__":
    main()
