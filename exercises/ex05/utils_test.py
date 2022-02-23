"""Testing the 'Utils' file."""

__author__ = "730474722"


from utils import only_evens
from utils import sub
from utils import concat
from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    numbers: list[int] = list()
    assert only_evens(numbers) == []


def test_only_evens_with_odd_numbers() -> None:
    numbers: list[int] = [3, 9, 15]
    assert only_evens(numbers) == []


def test_only_evens_with_even_numbers() -> None:
    numbers: list[int] = [2, 4, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_with_odd_and_even_numbers() -> None:
    numbers: list[int] = [2, 3, 4, 6, 9, 15]
    assert only_evens(numbers) == [2, 4, 6]


def test_sub_over() -> None:
    a_list: list[int] = [2, 4, 5, 6]
    assert sub(a_list, 0, 2) == [2, 4, 5]


def test_sub_under() -> None:
    a_list: list[int] = [2, 4, 5, 6]
    assert sub(a_list, 1, 3) == [4, 5, 6]


def test_sub_over_and_under() -> None:
    a_list: list[int] = [2, 4, 5, 6]
    assert sub(a_list, 1, 2) == [4, 5]


def test_sub_out_of_range() -> None:
    a_list: list[int] = [2, 4, 6]
    assert sub(a_list, -2, 2) == [2, 4, 6]


def test_concat_ascending() -> None:
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_descending() -> None:
    list_one: list[int] = [6, 5, 4]
    list_two: list[int] = [3, 2, 1]
    assert concat(list_one, list_two) == [6, 5, 4, 3, 2, 1]


def test_concat_same_number() -> None:
    list_one: list[int] = [2, 2, 2] 
    list_two: list[int] = [2, 2, 2]
    assert concat(list_one, list_two) == [2, 2, 2, 2, 2, 2]


def test_concat_mixed_numbers() -> None:
    list_one: list[int] = [3, 1, 2]
    list_two: list[int] = [5, 4, 6]    
    assert concat(list_one, list_two) == [3, 1, 2, 5, 4, 6] 


    


