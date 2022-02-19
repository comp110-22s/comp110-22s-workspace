"""Testing the functions from EX05."""

__author__: str = "730466987"

# Testing command: python -m pytest exercises/ex05

from exercises.ex05.utils import only_evens


def test_only_evens_empty() -> None:
    t1: list[int] = list()
    assert(only_evens) == t1

# In O.H., how would I get this function to work?


def test_only_evens_floats() -> None:
    t2: list[int] = list[float]
    assert(only_evens) == t2


def test_only_evens_four_odds() -> None:
    t3: list[int] = list()
    assert(only_evens) == t3

# for pt. 2

# def ________ -> None:
#     ta: ______
#     assert(only_evens) == ta

# def ________ -> None:
#     tb: ______
#     assert(only_evens) == tb

# def ________ -> None:
#     tc: ______
#     assert(only_evens) == tc

# for pt. 3

# def ________ -> None:
#     tx: ______
#     assert(only_evens) == tx

# def ________ -> None:
#     ty: ______
#     assert(only_evens) == ty

# def ________ -> None:
#     tz: ______
#     assert(only_evens) == tz