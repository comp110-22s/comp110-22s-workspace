"""Tests for linked list utils."""

import pytest
from typing import Optional
from exercises.ex10.linked_list import scale, Node, last, value_at, max, linkify, is_equal

__author__ = "730405989"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value at of an empty linked list should raise error."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_base() -> None:
    """Test base case, where index is 0."""
    assert value_at(Node(10, Node(20, Node(30, None))), 0) == 10


def test_value_at_complex() -> None:
    """Test base case, index not 0."""
    assert value_at(Node(10, Node(20, Node(30, None))), 1) == 20


def test_max_None() -> None:
    """Test empty Node."""
    with pytest.raises(ValueError):
        max(None)


def test_max_regular() -> None:
    """Test base case with one loop."""
    node: Node = Node(10, None)
    assert max(node) == 10


def test_max_longcase() -> None:
    """Test longer example."""
    node: Node = Node(10, Node(20, Node(30, None)))
    assert max(node) == 30


def test_link_empty() -> None:
    """Test empty list."""
    empty_list: list = []
    assert linkify(empty_list) is None


def test_complex_case() -> None:
    """Test more complex example."""
    s: Optional[Node] = linkify([1, 2, 3])
    t: Node = Node(1, Node(2, Node(3, None)))
    assert is_equal(s, t)


def test_empty_scale() -> None:
    """Test empty Node."""
    assert scale(None, 5) is None


def test_scale_complex() -> None:
    """Test more complex Node."""
    node_1: Optional[Node] = scale(linkify([1, 2, 3]), 2)
    node_2: Node = Node(2, Node(4, Node(6, None)))
    assert is_equal(node_1, node_2)
