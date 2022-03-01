"""Testing dictionary functions."""

__author__ = "730405989"

from exercises.ex06.dictionary import count, favorite_color, invert
import pytest


def test_emptyinvert() -> None:
    """Test that empty list is inverted to nothing."""
    assert invert({}) == {}


def test_invert1() -> None:
    """Invert value that is itself among others."""
    assert invert({"fan": "fan", "socks": "black", "pants": "yellow"}) == {"fan": "fan", "black": "socks", "yellow": "pants"}


def test_invert2() -> None:
    """Test regular inversion that is long, with varying strings of different sizes."""
    invtestdict: dict[str, str] = {"a": "letter", "lion": "animal", "couch": "furniture"}
    assert invert(invtestdict) == {"letter": "a", "animal": "lion", "furniture": "couch"}


def test_raising_keyerror() -> None:
    """Test that raises key error if values repeat."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_emptycolor() -> None:
    """If given empty color dictionary, return statement that points out there is no favorite color."""
    assert favorite_color({}) == 'No favorite color'


def test_color1() -> None:
    """Test dictionary where multiple are tied."""
    colortest1: dict[str, str] = {"Max": "green", "Ben": "blue", "Sam": "red", "Tom": "blue", "Lisa": "red"}
    assert favorite_color(colortest1) == 'blue'


def test_color2() -> None:
    """Test where dictionary has to change at last string to new favorite."""
    colortest2: dict[str, str] = {"a": "yellow", "b": "orange", "c": "blue", "d": "orange", "e": "red", "f": "red", "g": "blue", "h": "red"}
    assert favorite_color(colortest2) == 'red'


def test_emptycount() -> None:
    """If given empty list, return empty dictionary."""
    assert count([]) == {}


def test_count1() -> None:
    """Regular case with multiple counts."""
    testlist: list[str] = ["how", "many", "woulds", "would", "a", "would", "chuck", "chuck", "."]
    assert count(testlist) == {"how": 1, "many": 1, "woulds": 1, "would": 2, "a": 1, "chuck": 2, ".": 1}


def test_count2() -> None:
    """With one string of many counts, make sure does not replicate."""
    onestring: list[str] = ["max", "max", "max", "max", "max", "max", "max"]
    assert count(onestring) == {"max": 7}