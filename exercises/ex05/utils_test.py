"""Pytests for ex05."""

__author__ = "730465187"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_basic() -> None:
    """Basic test for only_evens function to make sure it returns evens in a short list."""
    nums: list[int] = [3, 6, 22]
    assert only_evens(nums) == [6, 22]


def test_only_evens_complex() -> None:
    """More complex test for only_evens function to make sure it returns evens in a longer list."""
    nums: list[int] = [21, 32, 56, 89, 100, 1001]
    assert only_evens(nums) == [32, 56, 100]


def test_only_evens_edge() -> None:
    """Edge case test that makes sure even negatives and 0 return even for only_evens function."""
    nums: list[int] = [-2, 0, 1, 2]
    assert only_evens(nums) == [-2, 0, 2]


def test_sub_simple() -> None:
    """Simple test for sub function to make sure it works with basic starting indexes."""
    numbs: list[int] = [1, 2, 3]
    start: int = 0
    end: int = 1
    assert sub(numbs, start, end) == [1]


def test_sub_complex() -> None:
    """Complex test for sub function to make sure it works with more complicated starting indexes."""
    numbs: list[int] = [23, 45, 67, 43, 876, 12, 987, 123, 67]
    start: int = -4
    end: int = 5
    assert sub(numbs, start, end) == [23, 45, 67, 43, 876]


def test_sub_edge_case() -> None:
    """Edge case test for sub function that makes sure if the starting index is beyond the length of the list, an empty list is returned."""
    numbs: list[int] = [1, 2, 5, 16, 21]
    start: int = 6
    end: int = 7
    assert sub(numbs, start, end) == []


def test_concat_simple() -> None:
    """Simple test for concat funcion to make sure it combines two strings."""
    L1: list[int] = [1, 2, 3]
    L2: list[int] = [4, 5, 6]
    assert concat(L1, L2) == [1, 2, 3, 4, 5, 6]


def test_concat_complex() -> None:
    """Complex test for concat function that does the same thing as the simple test with longer lists."""
    L1: list[int] = [4, 3, 5]
    L2: list[int] = [4, 1, 33, 6, 897]
    assert concat(L1, L2) == [4, 3, 5, 4, 1, 33, 6, 897]


def test_concat_edge() -> None:
    """Edge case test for concat function that makes sure the program runs right with an empty list as input."""
    L1: list[int] = []
    L2: list[int] = [1, 4, 16, 91]
    assert concat(L1, L2) == [1, 4, 16, 91]