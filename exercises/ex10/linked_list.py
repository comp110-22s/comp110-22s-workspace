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

# Remember that each recursion needs to go through specific steps to get closer to a base case! If specific steps aren't followed in each elif statement, you will either get
# and infinite loop or the "None" base case (which may miss returning the desired value).


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Tests if two Linked Lists have the same values and order as one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)

# This function says that, if head is not None, it will return the data point right before head is None.
# The else statement is there to ensure recursion through the whole Linked List up to that point.


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)

# This function says that, if the 2 base cases aren't met (if and elif), then it will go to "else" and decrease the index by 1 for every 1 data point that it moves through
# in the Linked List.

# This way, the index can maintain its relative position in a Linked List of any length.


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of the node found at the given index, if it exists."""
    if head is None:
        raise IndexError("Index does not exist in the list.")
    elif index == 0:
        return head.data
    else:
        index = index - 1
        return value_at(head.next, index)


# With max, there are 2 base cases and 2 recursive cases.

# The first "if" checks for the most basic base case: the whole Node being None.

# The 1st "elif" says, if the first base case isn't true, there is a second base case if the Node only contains 1 data point. In that case, you only have 1 data point to work with,
# so that's the point that gets returned.

# The 2nd "elif" checks the most recent data point in the Node against the ENTIRE rest of the Node to see if it has the greatest value.

# And, the "else" case just tells the program to recur again for each subsequent data point.

# Overall, for a Node like "1 -> 3 -> 2 -> None," the function will recur 2 separate times. It will check "1" against the rest of the Linked List, then "3".
# Once it hits 3, it will check it against the rest of the list ("2" and None) and print 3 as the greatest int value.

def max(head: Optional[Node]) -> int:
    """Returns the highest data value in the Linked List."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        return head.data
    elif head.data > max(head.next):
        return head.data
    else:
        return max(head.next)


# With linkify, the if statement is setting up a base case, in case the input list is empty.
# The else statement is saying that, if the list is not empty, each recursion should add the next unscanned node to the list,
# and to worry about the rest of the list values in the next recursion.

# Also, note that the slice notation on line 113 is telling the program to ignore everything from index 1 to the end of the list.
# With each recursion, the value at index 1 gets moved back, so it will always apply to the next value in the list, until it hits the last item and 1 = None.

# The if condition on line 107 could also be written as "not input_list" and mean the same thing as "if the list is empty."


def linkify(input_list: list[int]) -> Optional[Node]:
    """Converts a list of ints into a Linked List with the same values in the same order."""
    if len(input_list) == 0:
        return None
    else:
        new_node: Optional[Node] = Node(0, None)

        new_node.data = input_list[0]
        new_node.next = linkify(input_list[1:])

        return new_node

# In this function, the if statement sets up the base case, and the else statement says that, for each data point in head,
# it will create a new Node to store that data point * factor, and the "next" value will be the "scaled" function recurring with the rest of the list,
# including the next data point (which will also be multiplied by "factor").


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a linked list version of head where each data point is repeated "factor" times."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))