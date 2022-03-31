"""This is an example of Point OOP object (following LS24 and LS25)."""

from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """This function initializes a Point with its x and y values."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """This function mutates the inputes by multiplying them by a set factor."""
        self.x += factor
        self.y += factor

    def scale(self, factor: float) -> Point:
        """This function multiplies its components by the set factor."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """This function produces a high-level str representation of a Point."""
        return f"({self.x} {self.y})"

    def __repr__(self) -> str:
        """This function produces a str representtion of a Point, just like '__str__.'"""
        return f"Point({self.x}, {self.y})"

    def __mul__(self, factor: float) -> Point:
        """Overload that allows a Point to be multiplied by a float."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload that allows a Point to be added to another Point."""
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        "Overload for subscription notation (ex. a[0])."
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError
        

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])