"""Test for Part 1 of ex05."""

__author__ = 730486473
    
from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Test for only_evens function."""
    a: list[int] = [222]
    assert only_evens(a) == [222]


def test_sub() -> None:
    """Test for sub function."""
    a: list[int] = [10, 20, 30, 40]
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == [20, 30]


def test_concat() -> None:
    """Test for concat function."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: list[int] = [6, 7, 8, 9, 10]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
