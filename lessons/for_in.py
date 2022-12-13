"""An example of for in syntax."""

names: list[str] = ["Max", "Aaron", "Josh", "Grayson"]

# Example of iterating through names using a while loop
print("while output:")
i: int = 0
while i < len(names):
    game: str = names[i]
    print(game)
    i += 1

print("for loop output:")
# The following for...in loop is the same as the while loop
for name in names:
    print(name)


data_set: list[int] = [2, 53, 734, 1234]
ds_sum = 0
for value in data_set:
    ds_sum += value
    print(ds_sum)

print(ds_sum)
