# """Pytests for quiz 02 review."""


# from lessons.quiz_02 import odd_and_even, vowels_and_threes, average_grades


# def test_odd_and_even_simple() -> None:
#     a_list: list[int] = [2, 9, 4, 17, 9, 10, 15, 13, 14, 21]
#     assert odd_and_even(a_list) == [9, 15]


# def test_vowels_and_threes() -> None:
#     a: str = ("aeiou")
#     assert vowels_and_threes(a) == "eiu"


# def test_average_grades() -> None:
#     original: dict[str, list[int]] = {'Bill': [76, 94, 97], 'Annie': [88, 93, 98]}
#     assert average_grades(original) == {'Bill': 89, 'Annie': 93}


colors: dict[str, str] = {'Brad': 'yellow', 'Tyson': 'black', 'Steve': 'black', 'Simon': 'black', 'Alvin': 'white', 'Theodore': 'blue'}
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
print(new_dict)
result: str = ""
value: int = 0
for item in new_dict:
    if new_dict[item] > value:
        value = new_dict[item]
        result = item

print(result)