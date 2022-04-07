"""This is the practice run through of programs that you will need to write for QU02."""

# 23.


from numpy import True


def odd_and_even(all_values: list[int]) -> list[int]:
    """Thus function takes a list of ints and returns all ints that are odd and at an even index."""
    i: int = 0
    current_number: int = all_values[i]
    valid_numbers: list = list()

    while i <= len(all_values):
        if current_number % 2 != 0 and i % 2 == 0:
            valid_numbers.append(all_values[i])

    return valid_numbers


# 24.


# def vowels_and_threes(input_string: str) -> str:
#     """This function takes an input string and returns its items that are either at an index that is a multiple of 3 or a vowel."""
#     i: int = 0
#     final_string: str = ""

#     if i // 3 == 0 or input_string[i] == "a", "e", "i", "o", or "u":
#         final_string += input_string[i]
#         i += 1
#     else:
#         i += 1
#     return final_string


# The class website's solution (which is objectively better)

def vowels_and_threes(input_string: str) -> str:
    """This function takes an input string and returns its items that are either at an index that is a multiple of 3 or a vowel."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    is_vowel: bool = False
    final_string: str = ""
    i: int = 0

    while i < len(input_string):
        is_vowel = False
        if input_string[i] in vowels:
            is_vowel = True
        elif i % 3 == 0:
            final_string += input_string[i]
        elif is_vowel:
            final_string += input_string[i]
        i += 1
    return final_string
        