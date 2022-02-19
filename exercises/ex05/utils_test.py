"""Pytests for ex05."""

__author__ = "730465187"

from exercises.ex05.utils import only_evens, sub, concat


def test_evens_basic() -> None:
    nums: list[int] = [1, 2, 3, 4]
    assert only_evens(nums) == [2, 4]


def test_evens_complex() -> None:
    nums: list[int] = [2, 33, 56, 89, 100, 1001]
    assert only_evens(nums) == [2, 56, 100]


def test_evens_edge() -> None:
    nums: list[int] = [-2, 0, 1, 2]
    assert only_evens(nums) == [-2, 0, 2]


def test_sub_simple() -> None:
    numbs: list[int] = [1, 2, 4, 5, 6]
    start: int = 1
    end: int = 3
    assert sub(numbs, start, end) == [2, 4, 5]


def test_sub_complex() -> None:
    numbs: list[int] = [23, 45, 67, 43, 876, 12, 987, 123, 67]
    start: int = -4
    end: int = 5
    assert sub(numbs, start, end) == [23, 45, 67, 43, 876, 12]


def test_sub_edge_case() -> None:
    numbs: list[int] = [1, 2, 5, 16, 21]
    start: int = 6
    end: int = 7
    assert sub(numbs, start, end) == []


def test_concat_simple() -> None:
    L1: list[int] = [1, 2, 3]
    L2: list[int] = [4, 5, 6]
    assert concat(L1, L2) == [1, 2, 3, 4, 5, 6]


def test_concat_complex() -> None:
    L1: list[int] = [4, 3, 5]
    L2: list[int] = [4, 1, 33, 6, 897]
    assert concat(L1, L2) == [4, 3, 5, 4, 1, 33, 6, 897]


def test_concat_edge() -> None:
    L1: list[int] = []
    L2: list[int] = [1, 4, 16, 91]
    assert concat(L1, L2) == [1, 4, 16, 91]