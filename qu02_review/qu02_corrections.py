"""This is a review of different subquestions from QU02."""

# 1.4
# (You CHANGE a global variable through the "global" keyword, but you can ACCESS it just by calling it in a function.)


# 2
d: dict[str, int] = {"Pink": 10, "Black": 4, "Green": 3}


# 2.1

d["Red"] = 5

# To add the value for "Red" to this list, you can't use the ".append" command, because that is for lists.
# Instead, you define "Red" as a new key and declare its value on its own.


# 2.2

d.pop("Green")


# 2.3

d["Pink"] += 2


# 2.4

print(len(d))

# With the above command, don't forget to include the paranthesis around both "len" and "d"!


# 3.2 and 3.3


def main() -> None:
    a: list[int] = [1, 2, 3]
    print(f2(a))


def f1(xs: list[int]) -> list[int]:
    result: list[int] = []

    for item in xs:
        result.append(item * 2)
    return result


def f2(xs: list[int]) -> list[int]:
    """This function mutates the input list. Keep in mind that f1 and main are not included in this explanation, but they are included in the same problem."""
    i: int = 0
    
    while i < len(xs):
        if xs[i] % 2 == 0:
            xs[i] = xs[i] // 2
        else:
            xs[i] = 3 * xs[i] + 1
        i += 1
    return xs


main()

# If (f1(a)) were put in line 5, it would return [8, 2, 20] because it would multiply every item in the f2(a) list,
# [4, 1, 10], by 2.

# And the (f2(a)) list would be [4, 1, 10] in the first place because its i value would go up to 3, and because the list
# is 4 items long, the last value in a (which is 3) would be multiplied by 3 (making 9), and 1 would be added to that number
# (making it 10).


# 3.4

# In this case, "main"'s RA would be 27, f1's would be 3, and f2's would be 4.

# Also, note that the RV of f2 an the "xs" value for f2 are references to the same list ("a" in main).


# 4.1

# This function creates a dictionary with the items from list "x" as keys and the items from list "y" as values.


# 4.3

# ALSO, note that the function from problem 4 has duplicate keys on puporse; the end values of "y" (the repeated key) should just be "yummy"
# by the end of the function declaration.


# 4.4

# Also, for function 4, "main"'s RA is 21, and "zip"'s is 4.


# 5


def filter_by_last(word: list[str], char: str) -> list[str]:
    """This function makes a list of str where the last char in word matches the input char."""
    matching_char: list[str] = []

    for char in word:
        if len(word) - 1 == char:
            matching_char += char
    return matching_char

# 6


def grocery_shop(available: dict[str, int], wanted: dict[str, int]) -> list[str]:
    """This function creates a list of str that contains all items matching between both input lists."""
    bought: list[str] = []

    for key in wanted:
        if key in available and wanted[key] <= available[key]:
            bought += key

    return bought