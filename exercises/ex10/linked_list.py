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

# In O.H.: How do I resolve the TypeErrorwith head.data being included as an int parameter on line 55?

def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the node found at the given index, if it exists."""
    if head is None:
        raise IndexError("Index does not exist in the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.data, index)

# Also in O.H.: do I need to add an elif statement below to make a list of each data value and THEN find the max from that? 
# Or will it auomatically be interpreted if I leave it as return max(head)?


def max(head: Node) -> int:
    """Returns the highest data value in the Linked List."""
    if head is None:
        raise ValueError("Cannot call mas with None")
    else:
        return max(head)

# def linkify()

# def scale()