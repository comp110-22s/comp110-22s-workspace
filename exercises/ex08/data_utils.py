"""Some dictionary-related utility functions."""

__author__ = "730466987"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """This function reads the rows of a csv file into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """This function makes a list of values for input column keys."""
    result: list[str] = []
    
    for key in table_rows:
        item: str = key[column_name]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """This function makes a column-oriented table from an input row-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]

    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

# (The above 3 functions were covered during lecture; all new functions are below!)


def head(input_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """This function produces a column-based data table containing the first n rows of a row-based table."""
    final_table: dict[str, list[str]] = {}

    # Remember, it's better to use a while loop here because it's more efficient than saying something like "for input_table[column] in input_table."
    # Also, remember the difference between the syntax for adding things to dicts vs to lists! Dicts: dict_name[key] = value; Lists: list_name.append(value).

    # The "[column][i]" notation is new, but it just means that the values for the columns and for i (which are the rows) in input_table will both be added to the list.

    # NOTE: You can't add straight to the final dict from the input dict because of how they are oriented; it's easier to look for the values of interest in the row-based
    # table, and THEN add those values of interest to the column-based table.

    for column in input_table:
        first_row_values: list[str] = []
        i: int = 0

        while i < rows:
            first_row_values.append(input_table[column][i])
            i += 1

        final_table[column] = first_row_values

    return final_table

# With "select," remember that the values of interest are added from the input list to the values of the input table!


def select(input_table: dict[str, list[str]], new_column_names: list[str]) -> dict[str, list[str]]:
    """This function returns a column-based function from a subset of columns in the input table."""
    combined_table: dict[str, list[str]] = {}

    for column in new_column_names:
        combined_table[column] = input_table[column]

    return combined_table


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function produces 1 column-based function by combining 2 column-based functions."""
    final_dict: dict[str, list[str]] = {}

    for column in dict_1:
        final_dict[column] = dict_1[column]

    # This loop says that "if the item is in the dict, move past it; if it's not, add it."

    for column in dict_2:
        if column in final_dict:
            final_dict[column] += dict_2[column]
        else:
            final_dict[column] = dict_2[column]

    return final_dict

# Remember that in some cases (like the one below), a for-in loop is better than a while loop. HOWEVER, like above, sometimes a while loop is actually more useful 
# than a for-in loop. However, you don't need to avoid using a while loop just because we have learned about a different type of loop in class.


def count(finding_frequencies: list[str]) -> dict[str, int]:
    """This function will take a list and produce a dictionary where each key is an item in the list, and each value is the frequency of that item in the list."""
    frequencies: dict[str, int] = {}

    for column in finding_frequencies:
        if column in frequencies:
            frequencies[column] += 1
        else:
            frequencies[column] = 1

    return frequencies

# for the part after adding count...

# this function should take in the returned dicts from count SEPARATELY,
# loop through each dict,
# and find the key with the highest (most common) int in the input dict
# it should add the keys with the highest number values to a separate list[dict[str, int]].


def most_common(input_dict: dict[str, int]) -> list[dict[str, int]]:
    """This function returns the key with the highest value for each list item in the input dictionary."""
    most_common_values: list[dict[str, int]] = []
    highest_number_value: dict[str, int]

    # the function should start by taking in the entire dict and looping through each key
    # then it should add the key with the highest numerical value to the return dict
    # this process can be repeated with each of the 4 dicts from analysis.ipynb SEPARATELY

    for key in input_dict:
        if input_dict[key] > ____:
            highest_number_value += input_dict[key]

    return most_common_values