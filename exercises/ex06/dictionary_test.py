"""These are test that evaluate dictionaries."""

__author__: str = "730466987"

# The command to run your tests is python -m pytest exercises/ex06

from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_dupl_value() -> None:
    """This test prevents the invert function from returning duplicate values. (Use case.)"""
    dupl_list: dict[str, str] = {'one': '1', 'two': '1'}
    assert invert(dupl_list) == print("Please eliminate duplicate values.")


def test_invert_matching_names() -> None:
    """This test prevents invert from returning a set of key and value inputs with the same name. (Edge case.)"""
    same_name_list: dict[str, str] = {"x": "x"}
    assert invert(same_name_list) == print("No keys and values with matching names allowed. Please try again.")


def test_invert_blank_name() -> None:
    """This test prevents invert from returning a key or value input with a blank name. (Use case.)"""
    blank_dict: dict[str, str] = {"z" : ""}
    assert invert(blank_dict) == print("No nameless keys or values allowed. Please try again.")







# In O.H. (once all 3 functions are written out PLZ), see if you can fix this test so line 33 can do what the text says.

def test_favorite_color_tie() -> None:
    """This test returns the earlier key (color) in a dictionary if 2 colors are equally common. (Use case.)"""
    tie_dict: dict[str, str] = {"Joe": "pink", "Jane" : "green"}
    assert favorite_color(tie_dict) == # (however you can indicate that pink came first in the list)








def test_favorite_color_is_red() -> None:
    """This test guarantees that favorite_color will return red as the most common color in the dictionary. (Use case.)"""
    red_wins: dict[str, str] = {"Joe": "red", "Jane": "red", "Julia": "blue"}
    assert favorite_color(red_wins) == print("red")


def test_favorite_color_blank() -> None:
    """This test prevents favorite_color from processing a list where one of the keys has a blank value. (Edge case.)"""
    no_color: dict[str, str] = {"Jane": ""}
    assert favorite_color(no_color) != {"Jane", ""}



def test_count_empty_list() -> None:
    """This test prevents count from processing an empty list. (Edge case.)"""
    no_strs: list[str] = list()
    assert count(no_strs) == print("Cannot process an empty list. Please try again.")

def test_count_tie() -> None:
    """This test allows count to process a list with 2 strs of equal frequency. (Use case.)"""
    tie_list: list[str] = ["red", "red", "green", "green"]
    assert count(tie_list) == {"red": "2", "green": "2"}

def test_count_three_items() -> None:
    """This test allows count to process a list containing 3 terms. (Use case.)"""
    short_list: list[str] = ["red", "red", "blue"]
    assert count(short_list) == {"red": "2", "blue": "1"}