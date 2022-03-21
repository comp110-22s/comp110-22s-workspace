"""This is an example of for in syntax."""

names: list[str] = ["Naomi", "Emerson", "Tiffanie", "Gabby"]

# The following is an example of iterating through names using a while loop.
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# Versus using a for in loop...
for name in names:
    print(name)

# Using for in loops with the example from LS17:


def sum(xs: list[float]) -> float:
    "This function computes the sum of a list, the return value is nonsensical on purpose."
    total: float = 0.0
    for x in xs:
        total += x
    return total