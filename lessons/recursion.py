from __future__ import annotations

from typing import Union, Optional


class Node: 
    data: int
    # next: Union[Node, None]
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor of Node."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """String representation."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def sum(node: Optional[Node]) -> int:
    """Sum of all Nodes."""
    # if node.next == None:
    if node is None:
        return 0
    else:
        return node.data + sum(node.next)


def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)


head: Node = Node(3, None)
head = Node(2, None)
head = Node(1, head)
print(sum(head))
print(count(head))