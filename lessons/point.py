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
        """This function multiplies its compoenents by the set factor."""
        x: float = self.x * factor
        y: float = self.y * factor
        scaled_point: Point = Point(x, y)
        return scaled_point

    def __str__(self) -> str:
        """This function produces a high-level str representation of a Point."""
        return f"({self.x} {self.y})"

    def __repr__(self) -> str:
        """This function produces a str representtion of a Point, just like '__str__.'"""
        return f"Point({self.x}, {self.y})"


p0: Point = Point(1.0, 2.0)
p1: Point = p0.scale(2.0)
print(p0)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)