"""These are test that evaluate dictionaries."""

__author__: str = "730466987"

# The command to run your tests is python -m pytest exercises/ex06

from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_dupl_value() -> None:
    """This test prevents the invert function from returning duplicate values. (Use case.)"""
    dupl_list: dict[str, str] = {'one': '1', 'two': '1'}
    assert invert(dupl_list) == print("raise KeyError, please eliminate duplicate values.")


def test_invert_matching_names() -> None:
    """This test prevents invert from returning a set of key and value inputs with the same name. (Edge case.)"""
    same_name_list: dict[str, str] = {"x": "x"}
    assert invert(same_name_list) != same_name_list


def test_invert_blank_name() -> None:
    """This test prevents invert from returning a key or value input with a blank name. (Use case.)"""
    blank_dict: dict[str, str] = {"z" : ""}
    assert invert(blank_dict) != blank_dict


# In O.H. (once all 3 functions are written out PLZ), see if you can fix this test so line 33 can do what the text says.

def test_favorite_color_tie() -> None:
    """This test returns the earlier key (color) in a dictionary if 2 colors are equally common. (Use case.)"""
    tie_dict: dict[str, str] = {"Joe": "pink", "Jane" : "green"}
    assert favorite_color(tie_dict) == # (however you can indicate that pink came first in the list)


def test_favorite_color_red_and_blue() -> None:
    """This test guarantees that favorite_color will return red as the most common color in the dictionary. (Use case.)"""
    red_wins: dict[str, str] = {"Joe": "red", "Jane": "red", "Julia": "blue"}
    assert favorite_color(red_wins) == print("red")


def test_favorite_color_blank() -> None:
    """This test prevents favorite_color from processing a list where one of the keys has a blank value. (Edge case.)"""
    no_color: dict[str, str] = {"1": ""}
    assert favorite_color(no_color) != {"1", ""}


def test_count_____() -> None:
    """This test _____________. (Edge case.)"""
    assert count(__?__) == ______

def test_count_____() -> None:
    """This test _____________. (Edge case.)"""
    assert count(__?__) == ______

def test_count_____() -> None:
    """This test _____________. (Edge case.)"""
    assert count(__?__) == ______