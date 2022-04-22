"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730466987"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructs a singly Linked List. Uses None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produces a string visualization of the Linked List."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Tests if two Linked Lists have the same values and order as one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        return last(head.next)

        # How do I write this so that the program goes to the LAST node in the chain, and NOT the first?


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the node found at the given index, if it exists."""
    if head is None:
        raise IndexError("Index does not exist in the list.")
    else:
        return value_at(head.data, index)

# def max()

# def linkify()

# def scale()