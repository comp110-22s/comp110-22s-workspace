"""Example of a Point class."""
from __future__ import annotations


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initalize a Point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by factor."""
        self.x *= factor
        self.y *= factor

    # def scale(self, factor: float) -> Point:
    #     """Immutable: multiplies coponents by factor."""
    #     return Point(self.x * factor, self.y * factor)

    # def __str__(self) -> str:
    #     """Produce a str representation of a Point for humans."""
    #     print("""__str__ was called""")
    #     return f"({self.x}, {self.y})"

    # def __repr__(self) -> str:
    #     """Produce  a str representation of a Point for Python!"""
    #     return f"Point{self.x}, {self.y}"

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float.""" 
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Add stuff."""
        print("__add__ was called")
        return Point(self.x * rhs.x, self.y * rhs.y)

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    
p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 2.0
print(p0)
print(p1)
print(p0.__str__())
print(f"{p0.x}, {p0.y}")
print(f"{p1.x}, {p1.y}")
# COnstructor doing it for us
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)

# print(a[0])
# print(a[1])