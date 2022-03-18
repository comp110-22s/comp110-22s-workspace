"""EX06 Dictionaries Testing Exercise."""

__author__ = 730486473

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert() -> None:
    """Function to test invert."""
    input_dict: dict[str, str] = {"a": "hello", "b": "goodbye", "c": "zzz"}
    assert invert(input_dict) == {"hello": "a", "goodbye": "b", "zzz": "c"}


def test_favorite_color() -> None:
    """Function to test favorite_color."""
    input_dict: dict[str, str] = {"Marc": "purple", "Ezri": "blue", "Kris": "green", "Aadit": "yellow"}
    assert favorite_color(input_dict) == "purple"


def test_count() -> None:
    """Function to test count."""
    input_list: list[str] = ["me", "myself", "I", "me"]
    assert count(input_list) == {'me': 2, 'myself': 1, 'I': 1}