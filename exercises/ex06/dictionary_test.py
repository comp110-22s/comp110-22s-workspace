""""Testing for the dicionary exercise."""
__author__ = "730474722"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_with_single_key() -> None:
    """Tests the invert function with a single key."""
    carl = {"too fast": "way"}
    assert invert(carl) == {"way": "too fast"}


def test_invert_with_multiple_keys() -> None:
    """Tests the invert function when it has multiple keys"""
    lol = {"pen": "ren", "towel": "man", "cat": "dog", "lpopk": "plolok"}
    assert invert(lol) == {"ren": "pen", "man": "towel", "dog": "cat", "plolok": "lpopk"}


def test_invert_with_two_keys() -> None:
    """Tests the invert function when there are two keys."""
    opposites = {"blue": "red", "full": "hungry"}
    assert invert(opposites) == {"red": "blue", "hungry": "full"}


with pytest.raises(KeyError):
    """Returns a KeyError when there are duplicate keys."""
    mix_up = {"full": "stomach", "empty": "stomach"}
    invert(mix_up)


def test_favorite_color_with_single_item() -> None:
    """Returns the most picked color when thre is only one given.""" 
    Pablos_favorite = {"pablo": "green"}
    assert favorite_color(Pablos_favorite) == "green"


def test_favorite_color_when_equal_numbers_meet() -> None:
    """Returns the color that came first when more than one max color is equal."""
    colors = {"floor": "blue", "man": "green", "dog": "yellow", "cat": "blue", "cow": "green"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_with_multiple_items() -> None:
    """Returns the most reffered to color in a given dictionary."""
    colors = {"couch": "yellow", "sun": "yellow", "man": "green", "dog": "yellow", "cow": "green"}
    assert favorite_color(colors) == "yellow"


def test_count_with_multiple_higher_scores() -> None:
    """Returns the number of times each string is named."""
    kyle: list[str] = ["monster", "menace", "menace", "monster", "monster", "energy", "rage"]
    assert count(kyle) == {"monster": 3, "menace": 2, "energy": 1, "rage": 1}


def test_count_with_one_str_value() -> None:
    """Returns the appropriate count for one repeated str value."""
    clause: list[str] = ["santa", "santa", "santa", "santa"]
    assert count(clause) == {"santa": 4}


def test_count_back_and_forth() -> None:
    """Returns the appropriate count when two str values go back and forth."""
    christmas: list[str] = ["santa","claus", "santa", "claus", "santa", "claus", "santa", "claus"]
    assert count(christmas) == {"santa": 4, "claus": 4}
    