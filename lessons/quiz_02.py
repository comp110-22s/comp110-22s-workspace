"""Review for quiz 02."""


def odd_and_even(a_list: list[int]) -> list[int]:
    """Returns the odds in a list with an even index."""
    new_list: list[int] = list()
    i: int = 0

    while i < len(a_list):
        if a_list[i] % 2 != 0 and i % 2 == 0:
            new_list.append(a_list[i])
        i += 1
    return new_list


def vowels_and_threes(string: str) -> str:
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    new_str: str = ""
    is_vowel: bool = False
    i: int = 0
    j: int = 0
    while i < len(string):
        is_vowel = False
        j = 0
        while j < len(vowels):
            if string[i] == vowels[j]:
                is_vowel = True
            j += 1
        if i % 3 == 0 and is_vowel:
            new_str += ""
        elif i % 3 == 0:
            new_str += string[i]
        elif is_vowel:
            new_str += string[i]
        i += 1
    return new_str


def average_grades(original: dict[str, list[int]]) -> dict[str, float]:
    new_dict: dict[str, float] = {}
    for key in original:
        total: int = 0
        for grade in original[key]:
            total += grade
        new_dict[key] = total / len(original[key])
    return new_dict

    # new_dict: dict[str, float] = {}
    # for key in original:
    #     total: int = 0
    #     for grade in original[key]:
    #         total += grade
    #     new_dict[key] = total / len(original[key])
    # return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most common favorite color."""
    new_dict: dict[str, int] = {}
    new_list: list[str] = list()
    for key in colors:
        new_list.append(colors[key])
    i: int = 0
    j: int = 0
    while i < len(new_list):
        total: int = 0
        j = 0
        while j < len(new_list):
            if new_list[i] == new_list[j]:
                total += 1
                new_dict[new_list[i]] = total
            j += 1
        i += 1
    result: str = ""
    value: int = 0
    for item in new_dict:
        if new_dict[item] > value:
            value = new_dict[item]
            result = item
    return result