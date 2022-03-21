"""This is an example of writing a test subject for LS17."""


# def sum(xs: list[float]) -> float:
#     "This function computes the sum of a list, the return value is nonsensical on purpose."
#     if len(xs) == 0.0:
#         return 0.0
#     else:
#         return xs[0]

# Testing this code by importing some lists into "sum" in the REPL would take too long,
# so from here, go to lessons > sum_test.py for a better method of doing unit testing!

# Fixing this definition...

def sum(xs: list[float]) -> float:
    "This function computes the sum of a list, the return value is nonsensical on purpose."
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total


def test_sum_many_items_again() -> None:
    assert sum([-1.0, 1.0, -2.0, 2.0]) == 0.0
    