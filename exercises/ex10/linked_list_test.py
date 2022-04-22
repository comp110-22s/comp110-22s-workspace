"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last

# Testing command in the terminal: python -m pytest exercises/ex10/linked_list_test.py

__author__ = "730466987"

# for last


def test_empty_tail() -> None:
    """The last node of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_non_empty_tail() -> None:
    """The last node of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

# for value_at


def test_value_at_none_index() -> None:
    """The input index does not exist."""
    raise IndexError("Index does not exist in the list.")
    # Is it ok to have the same text from the actual function in the test? Or should this raise command only be found in 1 of them?


def test_value_at_zero_index() -> None:
    """The index of the function is 0, which is it's only other base case than it being None."""
    return value_at(head.data, 0)

# # for pt. 3

# def test_???______

# def test_???______

# # for pt. 4

# def test_???______

# def test_???______

# # for pt. 5

# def test_???______

# def test_???______