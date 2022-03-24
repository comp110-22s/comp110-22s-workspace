"""Testing the 'Utils' file."""


__author__ = "730474722"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Returns a empty list when given an empty list."""
    numbers: list[int] = list()
    assert only_evens(numbers) == []


def test_only_evens_with_odd_numbers() -> None:
    """Removes odd numbers in a list."""
    numbers: list[int] = [3, 9, 15]
    assert only_evens(numbers) == []


def test_only_evens_with_even_numbers() -> None:
    """Retains the even numbers in a list."""
    numbers: list[int] = [2, 4, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_with_odd_and_even_numbers() -> None:
    """Only removes odd numbers from a list with even and odd numbers."""
    numbers: list[int] = [2, 3, 4, 6, 9, 15]
    assert only_evens(numbers) == [2, 4, 6]


def test_sub_over() -> None:
    """Testing if sub removes the values in a list above the given y index."""
    a_list: list[int] = list()
    sub(a_list, 0, 1) == [1, 2]


def test_sub_under() -> None:
    """Testing if sub removes the values in a list below the given x index."""
    a_list: list[int] = [2, 4, 5, 6]
    sub(a_list, 1, 3) == [4, 5, 6]


def test_sub_over_and_under() -> None:
    """Testing sub when both given indexes are within the list."""
    a_list: list[int] = [1, 2, 3, 4]
    sub(a_list, 1, 2) == [2, 3]


def test_sub_empty_list() -> None:
    """Returns an empty list when given an empty list."""
    a_list: list[int] = list()
    sub(a_list, 0, 4) == []


def test_concat_ascending() -> None:
    """Testing an ascending list."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_descending() -> None:
    """Testing a descending list."""
    list_one: list[int] = [6, 5, 4]
    list_two: list[int] = [3, 2, 1]
    assert concat(list_one, list_two) == [6, 5, 4, 3, 2, 1]


def test_concat_same_number() -> None:
    """Testing for the same number."""
    list_one: list[int] = [2, 2, 2] 
    list_two: list[int] = [2, 2, 2]
    assert concat(list_one, list_two) == [2, 2, 2, 2, 2, 2]


def test_concat_mixed_numbers() -> None:
    """Testing for mixed numbers."""
    list_one: list[int] = [3, 1, 2]
    list_two: list[int] = [5, 4, 6]    
    assert concat(list_one, list_two) == [3, 1, 2, 5, 4, 6] 
