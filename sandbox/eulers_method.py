"""Euler's Method."""

h: float = 0.01
x: float = 0.0
y: float = 0.0


while x < 3.0:
    dydx: float = ((x) ** 2) + ((y) ** 2)
    y += h * dydx
    x = x + h
    print(x, y, dydx)