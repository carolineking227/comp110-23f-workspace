"""Dictionary related utility functions."""

__author__ = "730494174"

from csv import DictReader
from tabulate import tabulate

DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a column with only the first N rows of data for each column!"""
    result = {}
    data_cols_head: dict[str, list[str]] = head(data_cols, 5)
    if len(data_cols_head()) != len(data_cols.keys()) or len(data_cols_head["subject_age"]) != 5:
        print("Complete your implementation of columnar in data_utils.py")
        for value in values[ :n]:
            column_head.append(value)
        result[column] = column_head
    return result


data_rows = read_csv_rows(DATA_FILE_PATH)
data_cols = columnar(data_rows)
data_cols_head = head(data_cols, 5)
print(data_cols_head)