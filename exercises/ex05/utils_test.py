"""Where Tyler, The Creator and Childish Gambino test their sick beatz."""

__author__ = "730472535"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Tests and empty set."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_odds() -> None:
    """Tests a set with only odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Tests a full sets of mixed numbers."""
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(xs) == [0, 2, 4, 6, 8]


def test_sub_empty() -> None:
    """Tests an empty set with random inputs."""
    xs: list[int] = []
    a: int = 0
    b: int = 2
    assert sub(xs, a, b) == []


def test_sub_negative_start() -> None:
    """Tests with a negative input."""
    xs: list[int] = [1, 2, 3, 4, 5]
    a: int = -3
    b: int = 4
    assert sub(xs, a, b) == [1, 2, 3]


def test_sub_large_end() -> None:
    """Tests a large b variable greater than the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    a: int = 0
    b: int = 10
    assert sub(xs, a, b) == [1, 2, 3, 4, 5]


def test_concat_empty() -> None:
    """Base test for empty sets."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_empty_list_a() -> None:
    """Combines and empty list with a list."""
    a: list[int] = []
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3]


def test_concat_empty_list_b() -> None:
    """A is a full list b is empty."""
    a: list[int] = [1, 2, 3]
    b: list[int] = []
    assert concat(a, b) == [1, 2, 3]


def test_concat_full() -> None:
    """Both lists are full."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3, 1, 2, 3]