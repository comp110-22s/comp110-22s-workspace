"""This is a practice with recusrive functions that goes along with LS29."""

from __future__ import annotations

from typing import Optional


class Node:
    # This is an example of constructor recursion!
    data: int
    next: Optional[Node]
    # Which is the same as saying Union[Node, None] for next

    def __init__(self, data: int, next: Optional[Node]):
        """Initializes a Node object."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Turns the int output of a recursive function data into a str representation."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


# def sum(node: Node) -> int:
#     """Sums the data in a chain of Nodes."""
    # if node.next is None:
    #     return node.data
    # else:
    #     return node.data + sum(node.next)
    #     # This part of the function tells it to sum every data point in the chain after the Node with a value that != None :)
    #     # node.data is the value of the current node
    #     # node.next is the value of the previous node


# Simplified ver. with Optional[None]:
def sum(node: Optional[Node]) -> int:
    """Sums the data in a chain of Nodes."""
    if node is None:
        return 0
        # Here, the Optional parameter allows the program to look for a simplified base case, rather than checking every time to see if there is a following node that MIGHT be the base case.
    else:
        return node.data + sum(node.next)

# Recursive functions with recursive parameters (instead of just other nodes)...


def count(node: Node, current_count: int = 0) -> int:
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
print(count(head))
print(head)
# This last call outputs: "1 -> 2 -> 3 -> None"
# Cool!