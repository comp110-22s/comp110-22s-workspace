"""This teh lesson."""

from __future__ import annotations

from numpy import object0

class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving a and y args."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special method to represent objects as a string."""
        return f"{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplictation operator for point * float."""
        return Point(self.x * factor, self.y * factor)

    def scale(self, factor: float) -> Point:
        """Scale a point's attributes by a factor."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload the subscription notation."""
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
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