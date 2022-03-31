"""This is an example of using vectors that was used in the class lecture on 3/31/22."""

from __future__ import annotations

from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items):
        """Declares a new StrArray object."""
        self.items = items
    
    def __repr__(self) -> str:
        """Combines items from two different lists."""
        return f"StrArray ({self.items})"

        # __repr__ and __str__ are functionally the same for this class (as established in a previous lesson), but both are important functionally because
        # they allow you to access the class name in a print statement later, after it has been intialized.

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.
        When rhs is a str, it is concatenated to every item in a new StrArray.
        """
        # Establish a result list of str that is empty
        # Loop thorugh every item in self.items
        # Append the concatenation of item with rhs to the result list
        # After the loop completes, return a new StrArray object constructed with the result list
        result: list[str] = []

        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
                # Above, "self" = the lhs of the operator and, in this case, "!" = the rhs.
        else:
            # if isinstance(rhs, StrArray)

            for i in range(0, len(self.items)):
                # For the code above, know that it's basically the same as using a for-in loop to go through each item in the list.
                result.append(self.items[i] + " " + rhs.items[i])
                # The above line of code says that self and rhs are each applied to StrArray objects, and the "i"s line up their lists so that
                # self[1], for example, can only be added to rhs[1].
                # Also, there is a space added in the middle for easier reading of the print object.
        
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + last)

# Note that on line 18 above, writing print(first.__repr__) would do the same thing as the current command, but because __repr__ is called automagically, you don't
# need to include that much information to get the same output.

# A general note: you can't use multiple magic methods of the same name; here, you can only use "__add__" once.
# If you do define more than 1, the one defined later will be used as the model for everywhere it is called.