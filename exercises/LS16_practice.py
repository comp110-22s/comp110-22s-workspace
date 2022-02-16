"""This is a run-through of questions for LS16 on Gradescope (talking about global variables)."""

# #3

x: int = 0


def f() -> None:
    x: int = 1

f()
print(x)

# Basically, this code prints "0," because it calls the f function, but doesn't do anything with it.

# 6
x: int = 1


def f(y: int) -> int:
    return x + y


print(f(x + 1))

# This code prints "3," because it reads as "1 + 1." The first instance of x is 1, and x + 1 is 2, so y = 2.