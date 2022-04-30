"""This is a review of #6 from QU03 (function writing pt. 2)."""


# There are some issues with the inner loop, but I'm not sure how to fix them :(. )

class StringList:
    items: list[str]

    def __init__(self, items: list[str]):
        """Constructs a new StringList object."""
        self.items = items

    def __mul__(self, repeat: int) -> list[str]:
        new_str_list: list[str] = []

        i: int = 0

        while i < repeat:
            ii: int = 0

            while ii < len(self.items):
                new_str_list += self.items[i]
                ii += 1
            new_str_list[i] += self.items
            i += 1
        return new_str_list


x: StringList = StringList(["a", "b", "c"])
print(x.items)

print(x.__mul__(2))