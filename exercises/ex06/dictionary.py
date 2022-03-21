"""EX06 Dictionaries Exercise."""

__author__ = 730486473


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function to invert the key and key value in a dictionary."""
    final_dict: dict[str, str] = {}
    for key in input_dict:
        old_value: str = input_dict[key]
        if old_value in final_dict:
            raise KeyError("key already exists in final_dict!")
        final_dict[old_value] = key
    return final_dict
    

def favorite_color(input_dict: dict[str, str]) -> str:
    """Func to return the color that appears most frequently."""
    new_dict: dict[str, int] = {}
    new_list: list[str] = []
    i: int = 0
    for key in input_dict:
        new_list.append(input_dict[key])
    while i < len(new_list):
        if new_list[i] in new_dict:
            new_dict[new_list[i]] += 1
            i += 1
        else:
            new_dict[new_list[i]] = 1
            i += 1
    a_key = new_dict.get
    final_value = max(new_dict, key=a_key)
    return final_value


def count(input_list: list[str]) -> dict[str, int]:
    """Finds how many times a key is repeated."""
    new_dict: dict[str, int] = {}
    i: int = 0
    while i < len(input_list):
        if input_list[i] in new_dict:
            new_dict[input_list[i]] += 1
            i += 1
        else:
            new_dict[input_list[i]] = 1
            i += 1
    return new_dict