"""Working with dictionaries for ex 06."""

__author__: str = "730472535"


def invert(collection: dict[str, str]) -> dict[str, str]:
    """Swaps the key and value of a dictionary."""
    invert_dict: dict[str, str]  # New dictionary to serve as inverse
    invert_dict = dict()
    for key in collection:  # runs through each term in dictionary
        if collection[key] in invert_dict:
            raise KeyError("Key is a duplicate!")
        invert_dict[collection[key]] = key
    return invert_dict


def count(start_list: list[str]) -> dict[str, int]:
    """Takes a list and returns a dictionary with each term from the list and its multiplicity."""
    built_dict: dict[str, int]
    built_dict = dict()
    for item in start_list:
        if item in built_dict:
            built_dict[item] += 1
        else:
            built_dict[item] = 1
    return built_dict


def favorite_color(fav_color: dict[str, str]) -> str:
    """Fn returns the most popular term from a list."""
    counting_dict: dict[str, int]
    counting_dict = dict()
    for color in fav_color:
        if fav_color[color] in counting_dict:
            counting_dict[fav_color[color]] += 1
        else:
            counting_dict[fav_color[color]] = 1
    most_popular: int = 0
    return_color: str = ""
    for color in counting_dict:
        if counting_dict[color] > most_popular:
            most_popular = counting_dict[color]
            return_color = color
    return return_color
