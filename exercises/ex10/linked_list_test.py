"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale

__author__ = "730472535"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_wrong_index() -> None:
    """When index is too large, return IndexError."""
    with pytest.raises(IndexError):
        linked_list = Node(1, Node(2, Node(3, None)))
        value_at(linked_list, 3)


def test_value_at_empty() -> None:
    """Returns IndexError if an empty linked list is used."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at_normal_usage() -> None:
    """Returns the data at a specified Index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2
    

def test_max_empty() -> None:
    """Returns value error if head = None."""
    with pytest.raises(ValueError):
        max(None)


def test_max_normal() -> None:
    """Returns the greatest value in a linked list."""
    linked_list = Node(1, Node(3, Node(2, None)))
    assert max(linked_list) == 3
    

def test_max_negative() -> None:
    """Returns the greatest value in a linked list of negative numbers."""
    linked_list = Node(-1, Node(-3, Node(-2, None)))
    assert max(linked_list) == -1


def test_max_long_list() -> None:
    """Returns the greatest value in a linked list."""
    linked_list = Node(1, Node(100, Node(1000, Node(75, Node(50, None)))))
    assert max(linked_list) == 1000


def test_linkify_normal() -> None:
    """Returns a linked list in place of a regular list."""
    numbers: list[int] = [1, 2, 3]
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(linked_list, linkify(numbers))


def test_linkify_empty() -> None:
    """Returns None if start list is empty."""
    numbers: list[int] = []
    assert linkify(numbers) is None


def test_scale_empty() -> None:
    """If head is None return None."""
    assert scale(None, 1) is None


def test_scale_full() -> None:
    """Returns a new linked list with each piece of data scaled by `factor`."""
    linked_list = Node(1, Node(2, Node(3, None)))
    return_list = Node(2, Node(4, Node(6, None)))
    factor: int = 2
    assert is_equal(scale(linked_list, factor), return_list)


def test_scale_zero() -> None:
    """Returns a new linked list with each piece of data multiplied by 0."""
    linked_list = Node(1, Node(2, Node(3, None)))
    return_list = Node(0, Node(0, Node(0, None)))
    factor: int = 0
    assert is_equal(scale(linked_list, factor), return_list)