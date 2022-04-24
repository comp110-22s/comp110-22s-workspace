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
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the node found at the given index, if it exists."""
    if head is None:
        raise IndexError("Index does not exist in the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index)


def max(head: Node) -> int:
    """Returns the highest data value in the Linked List."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        return max(head)


# def linkify(head: list[int]) -> Optional[Node]:
#     """Converts a list of ints into a Linked List of Node values in the same order."""
#     if head is None:
#         return linkify(head.data)
#     else:
        
# How do you convert from a list to adding data to a chain of Nodes? (check the notes from last TShursday's lecture!!)

# def scale()