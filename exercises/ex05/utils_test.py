"""Testing the functions from EX05."""

__author__: str = "730466987"

# Testing command: python -m pytest exercises/ex05

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """This test makes only_evens return an empty list when the given list is empty."""
    assert only_evens([]) == list()


def test_only_evens_three_odds_one_even() -> None:
    """This test makes only_evens return an empty list when no even list items are given."""
    a_list: list[int] = [1, 3, 6, 7]
    assert only_evens(a_list) == list([6])

# In O.H., see if the below test is an edge case. If not, change it to something else plz.


def test_only_evens_floats() -> None:
    """This test makes only_evens return an empty list when the given list contains floats."""
    float_list: list[float] = [1.5, 2.5, 3.5, 4.0]
    assert only_evens(float_list) == list()

# In O.H., see if you can get the below test to work with a negative index, and see if you can get the "empty_list" and "empty_a" tests to have the correct syntax!


def test_sub_negative_start() -> None: 
    "This test makes sub start from index point 0 of a list with a negative start value."
    assert sub(-1, 2) == 


def test_sub_over_index() -> None:
    "This test makes sub end at the last index point of a list when stop_index is greater than the length of the list."
    short_list: list[int] = [0, 1, 2]
    assert only_evens(short_list) == [0, 1, 2]


def test_sub_empty_list() -> None:
    assert sub() == list()


def test_concat_empty_a() -> None:
    assert concat(list[], list[1, 2, 3]) == list()

def test_concat_both_empty() -> None:
    assert concat() == ty

def test_concat_float_list() -> None:
    tz: ______
    assert(only_evens) == tz