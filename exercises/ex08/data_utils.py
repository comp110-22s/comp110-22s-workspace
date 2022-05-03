"""Dictionary related utility functions."""

__author__ = "730472535"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read thefile as a csv rather than strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """A function that returns all the values in column 'key'."""
    return_list: list[str] = []
    for dictionary in table:
        for value in dictionary:
            if key == value:
                return_list.append(dictionary[key])
    return return_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Changes a table organizes as a list of rows to a table organized as a dict of columns."""
    return_dict: dict[str, list[str]]
    return_dict = dict()
    for column in table:  # column is a dictionary
        for key in column:  # key is a value for each term in dictionary
            return_dict[key] = column_values(table, key)
    return return_dict


def head(large_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """A function that returns n rows of a table."""
    small_table: dict[str, list[str]]
    small_table = dict()
    for column in large_table:  # each column is now a list
        n_values: list[str] = []
        for value in large_table[column]:
            if len(n_values) < n:
                n_values.append(value)
        small_table[column] = n_values
    return small_table


def select(large_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Creates a table with only specific columns."""
    return_dict: dict[str, list[str]]
    return_dict = dict()
    for item in names:
        return_dict[item] = large_table[item]
    return return_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """This combines two tables."""
    return_dict: dict[str, list[str]]
    return_dict = dict()
    for column in table_1:
        return_dict[column] = table_1[column]
    for column in table_2:
        if column in return_dict:
            for term in column:
                if term not in return_dict[column]:
                    return_dict[column].append(term)
        return_dict[column] = table_2[column]
    return return_dict


def count(values: list[str]) -> dict[str, int]:
    """This counts the frequency of each value from the list."""
    return_dict: dict[str, int]
    return_dict = dict()
    for item in values:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict


def average(columns: dict[str, int]) -> dict[str, float]:
    """Takes the average from a list of int 1-7."""
    total: int = 0
    number: int = 0
    i: int = 1
    return_dict: dict[str, float] = dict()
    for term in columns:  # term is a dict key
        while i <= 7:
            if term == str(i):
                total += len(columns[term]) * i
        i += 1
        number += columns[term]
        return_dict[term] = total / number
    return return_dict
    

def average2(table: dict[str, list[str]], key: str) -> float:
    """Takes the average from a list of int 1-7."""
    '''nt_list = list(map(int, string_list))'''
    ''' take out interseting and valuable columns using select'''
    '''for both you are goint to want to type cast using that thing'''
    '''then you have list of ints'''
    int_list = list(map(int, table[key]))
    return sum(int_list) / len(int_list)