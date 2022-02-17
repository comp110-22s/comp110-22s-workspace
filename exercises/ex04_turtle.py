"""Ski mountain."""

__author__ = "730405989"

from turtle import Turtle, colormode, done 

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    pen: Turtle = Turtle()
    # Pen is turtle variable because it is like a pen
    pen.color('gray')
    pen.left(90)
    draw_post(pen, 0, -250, 300)
    
    # regulation size basketball backboard is 182.9 X 126.9
    pen.begin_fill()
    draw_rect(pen, 91.45, 50, 182.9, 126.9)
    
    pen.color('black')
    pen.left(90)
    draw_rect(pen, -25, 100, 50, 40)

    # Basketball rim
    pen.color('orange')
    pen.right(90)
    draw_curve(pen, 25, 60, 75, 180)

    # Basketballs
    pen.right(90)
    pen.begin_fill()
    draw_curve(pen, -100, 0, 80, 360)
    pen.end_fill()

    # Basketball scoreboard
    draw_scoreboard(pen)

    done()


def goto_skip(pen: Turtle, x: float, y: float) -> None:
    """Function to run penup and move then pendown."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


# A little unneccesary, but only purpose to draw post, could draw other lines
def draw_post(pen: Turtle, x: float, y: float, height: float) -> None:
    """Function to draw post, also could be used to draw any other straight line."""
    goto_skip(pen, x, y)
    pen.forward(height)


def draw_rect(pen: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Function to draw rectangles of different widths and lenghts."""
    goto_skip(pen, x, y)
    i: int = 0
    # while loop to draw rectangle 
    while (i < 5):
        
        if i < 1:
            pen.left(90)
            pen.forward(width)
        else:
            pen.right(90)
            if i == 2:
                pen.forward(width)
            else:
                pen.forward(length)
        i = i + 1
    pen.end_fill()


def draw_curve(pen: Turtle, x: float, y: float, diameter: float, rotation: float) -> None:
    """Function that draws a curve by inching forward and rotating degree by degree."""
    goto_skip(pen, x, y)
    i = 0
    step: float = float(diameter / rotation)
    while i < rotation: 
        pen.forward(step)
        pen.right(1)
        i += 1
    

def draw_t(pen: Turtle, x: float, y: float, size: int) -> None:
    """Function that draws a T."""
    goto_skip(pen, x, y)
    pen.forward(size)
    pen.penup()
    pen.right(90)
    # Like this, a lot of the values are estimated, such as size/ 3 and were then trail and errored to see if they fit okay
    pen.forward(size / 3)
    pen.left(180)
    pen.pendown()
    pen.forward(size * 2 / 3)
    # 2/3 another estimate about letter t


def draw_e(pen: Turtle, x: float, y: float, size: int) -> None:
    """Function that draws an E."""
    goto_skip(pen, x + 5, y)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size / 3)
    goto_skip(pen, x + 5, y + (size / 2))
    pen.forward(size / 3)
    goto_skip(pen, x + 5, y)
    pen.forward(size / 3)
    # More trial and error trying to make letters not look horrible
    

def draw_a(pen: Turtle, x: float, y: float, size: int) -> None:
    """Function that draws A."""
    goto_skip(pen, x, y)
    pen.right(30)
    pen.forward(size)
    pen.right(135)
    pen.forward(size)
    goto_skip(pen, x + size / 4, y + size / 3)
    pen.left(75)
    pen.forward(size * 2 / 3)
    # This letter worst of all pretty estimated


def draw_m(pen: Turtle, x: float, y: float, size: int) -> None:
    """Function that draws M."""
    goto_skip(pen, x, y)
    pen.left(90)
    pen.forward(size)
    pen.right(135)
    pen.forward(size / 2)
    pen.left(90)
    pen.forward(size / 2)
    pen.right(135)
    pen.forward(size)
    # Pretty straightforward, just going forward, right, left etc...


def draw_1(pen: Turtle, x: float, y: float, size: int) -> None:
    """Function draws 1."""
    goto_skip(pen, x, y)
    pen.forward(size)
    pen.left(150)
    pen.forward(size / 2)


def draw_team(pen: Turtle, x: float, y: float) -> None:
    """Function that puts letter functions together to spell team."""
    draw_t(pen, x, y, 15)
    draw_e(pen, x + 8, y, 15)
    pen.left(90)
    draw_a(pen, x + 20, y, 15)
    draw_m(pen, x + 35, y, 15)
    # The adding gives space between letters


def draw_scoreboard(pen: Turtle) -> None:
    """Draw scoreboard, putting bunch of functions together."""
    pen.color(55, 118, 171)
    # Fill in scoreboard light blue
    pen.right(90)
    pen.penup()
    pen.goto(-300, 250)
    pen.begin_fill()
    draw_rect(pen, -300, 250, 200, 150)
    pen.end_fill()
    pen.left(90)
    pen.color('black')
    draw_team(pen, -280, 230)
    pen.right(180)
    draw_team(pen, -180, 230)
    # Draw team 2 times on different sides of scoreboard
    draw_rect(pen, -270, 220, 30, 30)
    pen.right(90)
    draw_rect(pen, -170, 220, 30, 30)
    pen.left(90)
    draw_1(pen, -255, 195, 15)
    pen.right(150)
    draw_1(pen, -155, 195, 15)
    # draws score section in scoreboard


main()