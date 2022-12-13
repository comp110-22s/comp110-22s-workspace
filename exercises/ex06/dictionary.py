"""Functions for EX06."""

__author__ = "730465187"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Returns an inverted dictionary."""
    new_dict: dict[str, str] = {}
    new_key: str = ""
    for key in original:
        new_key = original[key]
        new_dict[new_key] = key
    new_list: list[str] = list()
    # If the inverted dictionary has keys that are the same, this code raises a KeyError.
    for key in original:
        new_list.append(original[key])
    i: int = 0
    counter: int = 0
    while i < len(new_list):
        counter = 0
        while counter < len(new_list):
            if new_list[i] == new_list[counter] and i != counter:
                raise KeyError("You can't have two of the same key!")
            counter += 1
        i += 1
    return new_dict


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


"""Alternate, original code."""
# # Takes the colors and puts them in a list, new_list.
# new_list: list[str] = list()
# new_key: str = ""
# for key in original:
#     new_key = original[key]
#     new_list.append(new_key)
# # Creates a new dictionary, called new_dict, using the colors as the keys and the total amount of times the color appears in the list, new_list, as the value.
# new_dict: dict[str, int] = {}
# for item in new_list:
#     if item in new_dict:
#         new_dict[item] += 1
#     else:
#         new_dict[item] = 1
# # Takes every value in new_dict and puts them in a list, value_list.
# value_list: list[int] = list()
# value: int = 0
# for key in new_dict:
#     value = new_dict[key]
#     value_list.append(value)
# # Finds the maximum values of value_list by using the max function. Puts the value into last_list. If there are two values that are the same, they both get put in last_list.
# last_list: list[str] = list()
# for key in new_dict:
#     if new_dict[key] == max(value_list):
#         last_list.append(key)
# # The var, last_str, is created and returned. It represents the first index of last_list. This is either the color that is the most common response, or, if two+ colors are tied for most, the first to appear in the dictionary.
# last_str: str = last_list[0]
# return last_str

        

def count(original: list[str]) -> dict[str, int]:
    """Returns the total number of times a str occurs in a list."""
    result: dict[str, int] = {}
    for item in original:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def grocery_shop(inventory: dict[str, int], buy: dict[str, int]) -> list[str]:
    purchases: list[str] = []
    for product in inventory:
        for item in buy:
            if product == item:
                if inventory[product] >= buy[item]:
                    purchases.append(product)
    return purchases


# For the second part of this question, I think I deserve full credit. My code does test if the current item is a key in the first dict parameter in the line if product == item. It also tests if the current item's value in the second dict parameter is <= the current item's value in the first dict parameter, in the line if inventory[product] >= buy[item]. I've recreated my code in VS code and run multiple pytests with many different inventory and buy lists, and every one of them worked after I fixed the error in declaring my list. Even if my code does not exactly match the requirements in the second part of this question, it still works properly, so I'm not sure why I lost points.
