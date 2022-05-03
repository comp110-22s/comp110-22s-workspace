"""Tests for dictionary functions."""

__author__: str = "730472535"

from exercises.ex06.dictionary import invert
import pytest
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import favorite_color


def test_invert_one_value_set() -> None:
    """Tests a dictionary with only one term."""
    xs: dict[str, str] = dict()
    xs["dogs"] = "cats"
    assert invert(xs) == {"cats": "dogs"}


def test_invert_empty_set() -> None:
    """Edge case tests an empty set."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_invert_full_dict() -> None:
    """Tests a full dictionary."""
    xs: dict[str, str] = dict()
    xs["a"] = "z"
    xs["b"] = "y"
    xs["c"] = "x"
    assert invert(xs) == {"z": "a", "y": "b", "x": "c"}


with pytest.raises(KeyError):
    """Tests for a keyError."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_count_empty_list() -> None:
    """Edge case that tests an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_no_repetition() -> None:
    """Tests a list with no repetition."""
    xs: list[str] = ["a", "b", "c"]
    assert count(xs) == {"a": 1, "b": 1, "c": 1}


def test_count_with_repetition() -> None:
    """Tests a list with repetition."""
    xs: list[str] = ["a", "b", "c", "b", "b", "c"]
    assert count(xs) == {"a": 1, "b": 3, "c": 2}


def test_favorite_color() -> None:
    """Tests an empty list."""
    xs: dict[str, str] = dict()
    assert favorite_color(xs) == ""


def test_favorite_color_no_popular() -> None:
    """Tests a list with no repetition."""
    xs: dict[str, str] = dict()
    xs["max"] = "blue"
    xs["sam"] = "red"
    xs["cal"] = "pink"
    assert favorite_color(xs) == "blue"


def test_favorite_color_popular() -> None:
    """Tests a list with color repetition."""
    xs: dict[str, str] = dict()
    xs["max"] = "blue"
    xs["sam"] = "red"
    xs["cal"] = "pink"
    xs["hugh"] = "pink"
    xs["claire"] = "pink"
    xs["brett"] = "blue"
    assert favorite_color(xs) == "pink"