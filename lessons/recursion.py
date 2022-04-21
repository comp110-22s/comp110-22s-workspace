"""This is a practice with recusrive functions that goes along with LS29."""

from __future__ import annotations

from typing import Union


class Node:
    # This is an example of constructor recursion!
    data: int
    next: Union[Node, None]

    def __init__(self, data: int, next: Union[Node, None]):
        """Initializes a Nide object."""
        self.data = data
        self.next = next


def sum(node: Node) -> int:
    """Sums the data in a chain of Nodes."""
    if node.next is None:
        return node.data
    else:
        return node.data + sum(node.next)
        # This part of the function tells it to sum every data point in the chain after the Node with a value that != None :)
        # node.data is the value of the current node
        # node.next is the value of the previous node

# Recursive functions with recursive parameters (instead of just other nodes)...


def count(node: None, current_count: int = 0) -> int:
    """Returns the number of nodes in a linked list."""
    if node.next is None:
        return current_count + 1
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)

# Now, let's write a functional recursion.

print(sum(head))