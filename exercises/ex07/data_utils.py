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



# In O.H. on 3/22, see what you need to the 2nd loop to make the identities of each value line up correctly!
# What can you do with "rows" there?


def head(input_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """This function produces a column-based data table containing the first n rows of a row-based table."""
    final_table: dict[str, list[str]] = {}

    for column in input_table:
        first_row_values: list[str] = []

        while rows <= len(column):
            first_row_values += rows

        first_row_values = final_table[column]

    return final_table

# The "select" function works logically, but not in the way it's supposed to! You still need to fix it.

# REMEMBER: this function should work after "head" is corrected!! Check through it's logic, just in case, though.


def select(input_table: dict[str, list[str]], new_column_names: list[str]) -> dict[str, list[str]]:
    """This function returns a column-based function from a subset of columns in the input table."""
    combined_table: dict[str, list[str]] = {}

    for column in new_column_names:
        combined_table[column] += input_table[column]

    return combined_table

# In O.H., also make sure that this function works after the above 2 functions have been fixed!


def concat(dict_1: dict[str, list[str]], dict_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function produces 1 column-based function by combining 2 column-based functions."""
    final_dict: dict[str, list[str]] = {}

    for column in dict_1:
        final_dict[column] = dict_1[column]

    for column in dict_2:
        if dict_2[column] in final_dict:
            dict_1[column] += dict_2[column]
        else:
            final_dict[column] = dict_2[column]

    return final_dict


# Figure out how to make the logic on line 109 sound! How do you say "if it's not in the list, add it; if it is in the list, increase its value in the list by 1?"

def count(finding_frequencies: list[str]) -> dict[str, int]:
    """This function will take a list and produce a dictionary where each key is an item in the list, and each value is the frequency of that item in the list."""
    frequencies: dict[str, int] = {}
    i: int = 0

    while i <= len(finding_frequencies):
        if finding_frequencies[i] in frequencies:
            finding_frequencies[i] += 1
            i += 1
        else:
            finding_frequencies[i] = 1
            i += 1

    return frequencies