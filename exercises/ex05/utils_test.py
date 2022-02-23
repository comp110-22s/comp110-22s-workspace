"""Testing the functions from EX05."""

__author__: str = "730466987"

# Testing command: python -m pytest exercises/ex05

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """This test makes only_evens return an empty list when the given list is empty. (Edge case.)"""
    empty_list: list[int] = list()
    assert only_evens(empty_list) == list()


def test_only_evens_three_odds_one_even() -> None:
    """This test makes only_evens return an empty list when no even list items are given. (Use case.)"""
    a_list: list[int] = [1, 3, 6, 7]
    assert only_evens(a_list) == list([6])


def test_only_evens_all_evens() -> None:
    """This test makes only_evens print a list containing all even numbers. (Use case.)"""
    perfect_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(perfect_list) == [2, 4, 6, 8, 10]

# In O.H., see if you can get the below test to work with a negative index!


def test_sub_negative_start() -> None: 
    "This test makes sub start from index point 0 of a list with a negative start value. (Use case.)"
    negative_list: list[int] = [1, 2, 3]
    assert sub(negative_list(-1), -1, 2) == [1]


def test_sub_over_index() -> None:
    "This test makes sub end at the last index point of a list when stop_index is greater than the length of the list. (Use case.)"
    short_list: list[int] = [0, 1, 2]
    assert only_evens(short_list) == [0, 1, 2]


def test_sub_empty_list() -> None:
    "This test makes sub return an empty list when given an empty list. (Edge case.)"
    no_list: list[int] = list()
    assert sub(no_list, 0, 1) == list()



def test_concat_empty_a() -> None:
    "This test makes concat return only the items in list_b if list_a is empty. (Edge case.)"
    empty_a_list: list[int] = list()
    full_b_list: list[int] = [1, 2, 3]
    assert concat(empty_a_list, full_b_list) == full_b_list


def test_concat_different_lengths() -> None:
    "This test makes concat return 2 lists, where the first one is longer than the second one, but they are printed in sequential order. (Use case.)"
    long_a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    short_b_list: list[int] = [1, 2]
    final_list: list[int] = list()
    i: int = 0

    while i < len(long_a_list):
        final_list.append(long_a_list[i])
        i += 1

    while i < len(short_b_list):
        final_list.append(short_b_list[i])
        i += 1

    assert concat(long_a_list, short_b_list) == final_list

def test_concat_same_order() -> None:
    "This test allows concat to add the items in list_b onto the end of list_a without putting them in numerical order. (Use case.)"
    list_a: list[int] = [1, 2, 4]
    list_b: list[int] = [3, 5]
    assert only_evens(list_a, list_b) == [1, 2, 4, 3, 5]