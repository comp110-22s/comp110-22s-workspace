"""Description of Scene."""

__author__ = 730486473

import random
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    leo: Turtle = Turtle()
    leo.speed(100)
    leo.hideturtle()
    frame_length: float = 700.0
    bottom_left_x: float = -350.0
    bottom_left_y: float = -300.0
    bottom_right_x = (bottom_left_x + frame_length)
    bottom_right_y = (bottom_left_y)
    top_right_x = (bottom_right_x)
    top_right_y = (bottom_right_y + frame_length)
    top_left_x = (bottom_left_x)
    top_left_y = (bottom_left_y + frame_length)
    draw_square(leo, bottom_left_x, bottom_left_y)
    draw_beach(leo, bottom_left_x, bottom_left_y)
    draw_ocean(leo, top_left_x, top_left_y)
    draw_sky(leo, top_left_x, top_left_y)
    draw_sun(leo, top_right_x, top_right_y)
    draw_shells(leo, bottom_left_x, bottom_left_y)
    done()


def draw_square(leo: Turtle, x: float, y: float) -> None:
    """Function to draw frame."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    i: int = 0
    """Drawing."""
    while i < 4:
        leo.forward(700)
        leo.left(90)
        i += 1


def draw_beach(leo: Turtle, x: float, y: float) -> None:
    """Function to draw beach."""
    leo.penup()
    leo.goto(x + 2.0, y + 2.0)
    leo.pendown()
    """Start of Coloring."""
    leo.begin_fill()
    leo.pencolor(243, 245, 165)
    leo.fillcolor(243, 245, 165)
    i: int = 0
    """Drawing."""
    while i < 2:
        leo.forward(696)
        leo.left(90)
        leo.forward(300)
        leo.left(90)
        i += 1
    """Finish drawing."""
    leo.end_fill()


def draw_ocean(leo: Turtle, x: float, y: float) -> None:
    """Function to draw the ocean."""
    leo.penup()
    leo.goto(x + 2.0, y - 198.0)
    leo.pendown()
    """Start of coloring."""
    leo.begin_fill()
    leo.pencolor(22, 73, 159)
    leo.fillcolor(22, 73, 159)
    i: int = 0
    """Drawing."""
    while i < 2:
        leo.forward(696)
        leo.right(90)
        leo.forward(200)
        leo.right(90)
        i += 1
    """Finish drawing."""
    leo.end_fill()


def draw_sky(leo: Turtle, x: float, y: float) -> None:
    """Function to draw the sky."""
    leo.penup()
    leo.goto(x + 2.0, y - 2.0)
    leo.pendown()
    """Start of coloring."""
    leo.begin_fill()
    leo.pencolor(149, 222, 238)
    leo.fillcolor(149, 222, 238)
    i: int = 0
    """Drawing."""
    while i < 2:
        leo.forward(696)
        leo.right(90)
        leo.forward(200)
        leo.right(90)
        i += 1
    """Finish Drawing."""
    leo.end_fill()


def draw_sun(leo: Turtle, x: float, y: float) -> None:
    """Function to draw sun."""
    leo.penup()
    leo.goto(x - 100.0, y - 125.0)
    leo.pendown()
    """Start of Coloring."""
    leo.begin_fill()
    leo.pencolor(251, 189, 1)
    leo.fillcolor(251, 189, 1)
    """Drawing."""
    leo.circle(50)
    """Ending."""
    leo.end_fill()


def draw_shells(leo: Turtle, x: float, y: float) -> None:
    """Trying to draw shells in a confined space."""
    z: int = 0
    while z < 20:
        a: float = random.uniform(x + 20, x + 670)
        b: float = random.uniform(y + 20, y + 270)
        leo.penup()
        leo.goto(a, b)
        leo.pendown()
        leo.begin_fill()
        leo.pencolor(219, 219, 219)
        leo.fillcolor(219, 219, 219)
        i: int = 0
        while i == 0:
            leo.forward(20)
            leo.right(120)
            leo.forward(20)
            leo.right(180)
            h: int = 0
            while h < 5:
                leo.forward(4)
                leo.left(120)
                leo.forward(4)
                leo.right(120)
                h += 1
            i += 1
        draw_blackshells(leo, a + 30, b + 30)
        z += 1
        leo.end_fill()


def draw_blackshells(leo: Turtle, x: float, y: float) -> None:
    """Function that is called multiple times."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.begin_fill()
    leo.pencolor(0, 0, 0)
    leo.fillcolor(0, 0, 0)
    i: int = 0
    while i == 0:
        leo.forward(20)
        leo.right(120)
        leo.forward(20)
        leo.right(180)
        h: int = 0
        while h < 5:
            leo.forward(4)
            leo.left(120)
            leo.forward(4)
            leo.right(120)
            h += 1
        i += 1
    leo.end_fill()
    

main()