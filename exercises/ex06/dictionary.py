"""Creating dictionary functions."""
__author__ = "730474722"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the key and the value in a given dictionary."""
    key_list = list()
    value_list = list()
    i = 0
    k = 0
    for key in x:
        key_list.append(key)
        value_list.append(x[key])
    while k < (len(value_list)):
        while i < len(value_list):
            if value_list[i] == value_list[k] and i != k:
                raise KeyError("Duplicate Keys.")
            else:
                i += 1
        k += 1
    inverted_dict = {}
    i = 0
    while i < len(key_list):
        inverted_dict[value_list[i]] = key_list[i]
        i += 1
    return inverted_dict


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most frequent color."""
    color_list = list()
    color_leaderboard: dict[str, int] = {}
    i: int = 0
    k: int = 0
    for keys in x:
        color_list.append(x[keys])
    for colors in color_list:
        color_leaderboard[colors] = 1
    while k < len(color_list):
        while i < len(color_list):
            if color_list[i] == color_list[k] and i != k:
                color_leaderboard[color_list[i]] += 1
                i += 1
            else:
                i += 1
        k += 1
    i = 0
    k = 0
    compact_color = list()
    for compacted_color in color_leaderboard:
        compact_color.append(compacted_color)
    while k < len(compact_color):
        if color_leaderboard[compact_color[i]] >= color_leaderboard[compact_color[k]]:
            k += 1
        else: 
            i += 1
    return compact_color[i]


def count(count: list[str]) -> dict[str, int]:
    """Returns a dictionary where each key is a unique value in a given list that is counted."""
    count_leaderboard: dict[str, int] = {}
    for values in count:
        if values in count:
            count_leaderboard[values] = 0
    i = 0
    while i < len(count):
        if count[i] in count_leaderboard:
            count_leaderboard[count[i]] += 1
        i += 1
    return count_leaderboard