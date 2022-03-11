"""An example of looping through all of the characters in a string, taught in LS09."""

user_string: str = input("Give me a string! ")

i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done! ")

# The variable "i" is a common variable name in programming.
# "i" = "iteration"/"iterate"
# It is usually used as a counting variable, and here, we will use it
# to count the number of characters in the index of an input string.

# Here, i = 0 at first, and then it increases with the length of the string.
# This is easier than writing n different repetitions of the same command, like
# in EX01, since we don't know how long the string will be this time.
# i = 0 (index at 0) before the loop, i = 1 (index at one) after 1 iteration, etc.