
"""Tests for linked list utils."""


import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730465187"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_simple() -> None:
    """Simple test for value_at function."""
    linked_list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
    assert value_at(linked_list, 4) == 5


def test_value_at_index_one() -> None:
    """Tests the base case of index being one for the value_at function."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_index_error() -> None:
    """Tests if value_at properly raises an index error."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_max_simple() -> None:
    """Simple test for max function."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_base_case() -> None:
    """Testing the max function for a node with only one value."""
    linked_list = Node(10, None)
    assert max(linked_list) == 10


def test_max_value_error() -> None:
    """Tests if the max function properly raises a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_simple() -> None:
    """Simple test for the linkify function."""
    l: list[int] = [1, 2, 3]
    assert str(linkify(l)) == "1 -> 2 -> 3 -> None"


def test_linkify_base() -> None:
    """Tests if the linkify function returns None for an empty list."""
    l: list[int] = []
    assert linkify(l) is None


def test_scale_simple() -> None:
    """Simple test for the scale function."""
    linked_list: Node = (Node(3, Node(2, Node(1, None))))
    assert str(scale(linked_list, 2)) == "6 -> 4 -> 2 -> None"


def test_scale_base() -> None:
    """Tests if the scale function returns None when head is None."""
    assert(scale(None, 1)) is None