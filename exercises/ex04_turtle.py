"""A poor attempt at drawing a frisbee game."""

__author__ = "730465187"

from random import randint

from turtle import Turtle, colormode, done
colormode(255)


def draw_background() -> None:
    """Creates the background for the scene. Breaks down the complex function of drawing the background into neater code."""
    background: Turtle = Turtle()
    background.speed(0)
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


def draw_field() -> None:
    """Draws the field the players are on. Breaks down the complex function of drawing the background into neater code."""
    field: Turtle = Turtle()
    field.speed(0)
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


def draw_moon(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function 1/4. Draws the background and field with a moon. Implements the functions draw_background and draw_field, which makes the code neater and easier to understand."""
    """Uses the randint function to decide which type of moon to draw - full moon, crescent moon, or no moon."""
    draw_background()
    draw_field()
    a_turtle.speed(0)
    a_turtle.pu()
    a_turtle.goto(x, y)
    a_turtle.pd()
    a_turtle.speed(100)
    a_turtle.color("black", "white")
    a_turtle.begin_fill()
    which_moon: int = randint(1, 3)
    i: int = 0
    if which_moon == 1:
        while (i < 60):
            a_turtle.forward(size * 3)
            a_turtle.left(3)
            i += 1
        a_turtle.setheading(-45)
        counter: int = 0
        while (counter < 33):
            a_turtle.forward(size * 4)
            a_turtle.left(-3)
            counter += 1
    elif which_moon == 2:
        while (i < 120):
            a_turtle.forward(size * 3)
            a_turtle.left(3)
            i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_frisbee(a_turtle: Turtle, x: float, y: float) -> None:
    """Function 2/4. Draws a frisbee of a random size 1-5."""
    size: int = randint(1, 5)
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.color("white", "white")
    i: int = 0
    while (i < 90):
        a_turtle.forward(size * .25)
        a_turtle.left(2)
        i += 1
    a_turtle.forward(size * 30)
    i = 0
    while (i < 90):
        a_turtle.forward(size * .25)
        a_turtle.left(2)
        i += 1
    a_turtle.forward(size * 30)
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_lights(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function 3/4. Draws the lights."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown
    a_turtle.begin_fill()
    a_turtle.color("gray")
    a_turtle.left(270)
    a_turtle.forward(size * 200)
    a_turtle.left(90)
    a_turtle.forward(20 * size)
    a_turtle.left(90)
    a_turtle.forward(200 * size)
    a_turtle.right(90)
    a_turtle.end_fill()

    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.color("white", "gray")
    a_turtle.pensize(5)
    i = 0
    while i < 60:
        a_turtle.forward(size * .5)
        a_turtle.left(3)
        i += 1
    a_turtle.forward(size * 25)
    i = 0
    while i < 60:
        a_turtle.forward(size * .5)
        a_turtle.left(3)
        i += 1
    a_turtle.forward(25 * size)
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_player(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function 4/4. Draws a player."""
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color(241, 156, 107)
    a_turtle.pensize(10)
    a_turtle.left(45)
    a_turtle.forward(size * 20)
    a_turtle.right(90)
    a_turtle.forward(size * 20)
    a_turtle.right(180)
    a_turtle.forward(size * 20)
    a_turtle.right(45)
    a_turtle.forward(size * 30)
    a_turtle.right(90)
    a_turtle.forward(size * 10)
    a_turtle.right(180)
    a_turtle.forward(size * 20)
    a_turtle.right(180)
    a_turtle.forward(size * 10)
    a_turtle.left(90)
    a_turtle.forward(size * 10)
    a_turtle.right(90)
    a_turtle.begin_fill()
    i = 0
    while (i < 120):
        a_turtle.forward(size * .25)
        a_turtle.left(3)
        i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def main() -> None:
    """The entrypoint of my scene."""
    moon: Turtle = Turtle()
    frisbee: Turtle = Turtle()
    lights: Turtle = Turtle()
    player: Turtle = Turtle()
    draw_moon(moon, 200, 200, 1)
    draw_frisbee(frisbee, 100, -200)
    draw_lights(lights, -300, -50, 1)
    draw_lights(lights, 250, -50, 1)
    draw_player(player, -250, -250, 1)
    draw_player(player, 200, -250, 1)

    done()


if __name__ == "__main__":
    main()