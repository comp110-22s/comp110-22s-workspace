"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last

# Testing command in the terminal: python -m pytest exercises/ex10/linked_list_test.py

__author__ = "730466987"

# for pt. 1

def test_empty_tail() -> None:
    """The last node of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_non_empty_tail() -> None:
    """The last node of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

# for pt. 2

def test_???______

def test_???______

# for pt. 3

def test_???______

def test_???______

# for pt. 4

def test_???______

def test_???______

# for pt. 5

def test_???______

def test_???______