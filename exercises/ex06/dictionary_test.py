"""These are test that evaluate dictionaries."""

__author__: str = "730466987"

# The command to run your tests is python -m pytest exercises/ex06

from dictionary import invert, favorite_color, count


def test_invert_matching_names() -> None:
    """This test allows invert to return a set of key and value inputs with the same name (Edge case)."""
    same_name_list: dict[str, str] = {"x": "x"}
    assert invert(same_name_list) == {"x": "x"}


def test_invert_dupl_value() -> None:
    """This test prevents the invert function from returning duplicate values (Use case)."""
    dupl_list: dict[str, str] = {'one': '1', 'two': '1'}
    assert invert(dupl_list) != dupl_list


def test_invert_blank_name() -> None:
    """This test prevents invert from returning a key or value input with a blank name (Use case)."""
    blank_dict: dict[str, str] = {"z": ""}
    assert invert(blank_dict) != {"z": ""}


def test_favorite_color_blank() -> None:
    """This test prevents favorite_color from processing a list where one of the keys has a blank value (Edge case)."""
    no_color: dict[str, str] = {"Jane": ""}
    assert favorite_color(no_color) != {"Jane", ""}


def test_favorite_color_tie() -> None:
    """This test returns the earlier color in a dictionary if 2 colors are equally frequent (Use case)."""
    tie_dict: dict[str, str] = {"Joe": "pink", "Jane": "green"}
    assert favorite_color(tie_dict) == "pink"


def test_favorite_color_is_red() -> None:
    """This test guarantees that favorite_color will return red as the most common color in the dictionary (Use case)."""
    red_wins: dict[str, str] = {"Joe": "red", "Jane": "red", "Julia": "blue"}
    assert favorite_color(red_wins) == ("red")


def test_count_empty_list() -> None:
    """This test allows count to process an empty list (Edge case)."""
    no_strs: list[str] = list()
    assert count(no_strs) == {}


def test_count_tie() -> None:
    """This test allows count to process a list with 2 strs of equal frequency (Use case)."""
    tie_list: list[str] = ["red", "red", "green", "green"]
    assert count(tie_list) == {"red": 2, "green": 2}


def test_count_three_items() -> None:
    """This test allows count to process a list containing 3 terms (Use case)."""
    short_list: list[str] = ["red", "red", "blue"]
    assert count(short_list) == {"red": 2, "blue": 1}