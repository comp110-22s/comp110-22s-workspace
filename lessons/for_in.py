"""An example of for in syntax."""

names: list[str] = ["kris", "cal", "hugh", "lindsey"]

# example of iterating through names using a while loop
i: int = 0
print("while output:")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for.. in loop is the same as a while loop
print("for in..out output")
for name in names:
    print(name)