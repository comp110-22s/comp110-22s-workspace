"""An example of a while loop statement from LS09."""

# Example 1
counter: int = 0
maximum: int = (int(input("Count up to, but not including what? ")))

while counter < maximum:
    print(counter)
    counter = counter + 1

print("Done!")

# Example 2
counter: int = 0
maximum: int = (int(input("Count up to, but not including what?")))

while counter < maximum:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")

# Note: with both of these possible calculations, the number of counting #s doesn't matter. You can calculate the square of
# every number between 0 and 10 or between 0 and 1000, and this program can do either; the amount of data doesn't matter
# even though what you do with it does matter.