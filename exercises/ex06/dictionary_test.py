"""Pytests for EX06."""

__author__ = "730465187"

from dictionary import invert, favorite_color, count, grocery_shop
import pytest

with pytest.raises(KeyError):
    original = {'Kris': 'Jordan', 'Michael': 'Jordan'}
    invert(original)


def test_invert_basic() -> None:
    """Basic test for invert function."""
    original = {'matthew': 'james', 'steve': 'young'}
    assert invert(original) == {'james': 'matthew', 'young': 'steve'}


def test_invert_complex() -> None:
    """More complex test for invert function."""
    original = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(original) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_edge() -> None:
    """An edge case test for invert."""
    original = {'': 'james', 'Kevin': ''}
    assert invert(original) == {'james': '', '': 'Kevin'}


def test_favorite_color_simple() -> None:
    """A simple test for the favorite color function."""
    original = {'Max': 'green', 'John': 'yellow', 'James': 'green'}
    assert favorite_color(original) == 'green'


def test_favorite_color_complex() -> None:
    """A more complex test for favorite color fuction."""
    original = {'Brad': 'yellow', 'Tyson': 'black', 'Steve': 'black', 'Simon': 'black', 'Alvin': 'white', 'Theodore': 'blue'}
    assert favorite_color(original) == 'black'


def test_favorite_color_edge() -> None:
    """An edge case test for favorite color function."""
    original = {'Ben': 'orange', 'Alex': 'purple', 'Matt': 'orange', 'Jason': 'purple', 'Kevin': 'orange', 'Andrew': 'purple'}
    assert favorite_color(original) == 'orange'


def test_count_simple() -> None:
    """A simple test for the count function."""
    original: list[str] = ["hi", "hi", "green", "orange", "orange", "hi"]
    assert count(original) == {'hi': 3, 'green': 1, 'orange': 2}


def test_count_complex() -> None:
    """A more complicated test for the count function."""
    original: list[str] = ["long", "long", "long", "long", "long", "yellow", "big", "big", "long"]
    assert count(original) == {'long': 6, 'yellow': 1, 'big': 2}


def test_count_edge() -> None:
    """Edge case test for function count."""
    original: list[str] = ["", "", " ", " ", " ", "wacky"]
    assert count(original) == {'': 2, ' ': 3, 'wacky': 1}


def test_grocery_shop_1() -> None:
    inventory: dict[str, int] = {"bread": 3, "chips": 1, "eggs": 5}
    buy: dict[str, int] = {"bread": 5, "chips": 1, "kiwis": 2}
    assert grocery_shop(inventory, buy) == ["chips"]


def test_grocert_shop_2() -> None:
    inventory: dict[str, int] = {}
    buy: dict[str, int] = {"milk": 1}
    assert grocery_shop(inventory, buy) == []


def test_grocery_shop_3() -> None:
    inventory: dict[str, int] = {"milk": 23, "fish": 22, "juice": 9}
    buy: dict[str, int] = {"fish": 23, "milk": 2, "juice": 2}
    assert grocery_shop(inventory, buy) == ["milk", "juice"]