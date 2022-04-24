"""Tests for linked list utils."""

import pytest
from typing import Optional

from exercises.ex10.linked_list import Node, last, value_at, max, linkify

# scale (put those lines together after these functions have been written!)

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


def test_value_at_zero_index() -> None:
    """The input index is at 0, the 2nd base case."""
    zero_index: Node = (Node(1, Node(2, Node(3, None))))
    assert value_at(zero_index, 0) == 1


def test_value_at_index_one() -> None:
    """The index of the function is 1."""
    one_index: Node = Node(2, Node(4, Node(6, None)))
    assert value_at(one_index, 1) == 4

# for max


def test_max_equal_values() -> None:
    """Multiple values are the max."""
    two_max: Node = Node(1, Node(2, Node(2, None)))
    assert max(two_max) == 2


def test_max_one_max() -> None:
    """One value is the max."""
    one_max: Node = Node(1, Node(2, Node(3, None)))
    assert max(one_max) == 3

# for linkify


def test_linkify_empty_list() -> None:
    """The input list is empty."""
    return None


def test_linkify_demo_list() -> None:
    """The input list is properly converted into a chain of Nodes."""
    demo_list: list[int] = [1, 2, 3]
    demo_node: Optional[Node] = Node(1, Node(2, Node(3, None)))
    assert linkify(demo_list) == demo_node


# for scale

# def test_???______

# def test_???______