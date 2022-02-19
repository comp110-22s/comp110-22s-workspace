"""Testing the functions from EX05."""

__author__: str = "730466987"

# Testing command: python -m pytest exercises/ex05

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    t1: list[int] = list()
    assert(only_evens) == t1


# In O.H., how would I get this function (t2) to work?


def test_only_evens_floats() -> None:
    t2: list[int] = list[float]
    assert(only_evens) == t2


def test_only_evens_four_odds() -> None:
    t3: list[int] = list()
    assert(only_evens) == t3


# for pt. 2


def test_sub_negative_start() -> None: 
    ta = sub[0]
    assert(sub)  == ta


def test_sub_over_index() -> None:
    tb: ______
    assert(only_evens) == tb


def test_sub_empty_list() -> None:
    tc: ______
    assert(sub) == tc


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