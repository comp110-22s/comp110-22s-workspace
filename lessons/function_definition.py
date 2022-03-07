"""This is an example of a function definition from LS13."""


def my_max(a: int, b: int) -> int:
    # This function should return the largest argument
    if a >= b:
        return a
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)