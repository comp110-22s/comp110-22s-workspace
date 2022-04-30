"""This is my response to #1 on the final prep question list (4/29/22)."""


def factorial(n: int) -> int:
    if n < 2:
        return 2
    else:
        return n * factorial(n - 1)


print(factorial(4))