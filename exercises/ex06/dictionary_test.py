"""EX07 dict unit tests!"""
__author__ = 730494174

from typing import List, Dict, Optional, Union
import unittest
from dictionary import invert, alphabetizer, favorite_color, count, update_attendance
import pytest


def invert(input_dict: Dict[str, str]) -> Dict[str, str]:
    """Invert the keys and values of a dictionary."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"KeyError: Duplicate value '{value}' encountered")
        inverted_dict[value] = key
    return inverted_dict


def test_invert_normal_case() -> None:
    """Test invert function with a normal use case."""
    input_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    result = invert(input_dict)
    assert result == {'apple': 'a', 'banana': 'b', 'cherry': 'c'}, "Invert function failed for normal case."


def test_invert_empty_dict() -> None:
    """Test invert function with an empty dictionary."""
    input_dict = {}
    result = invert(input_dict)
    assert result == {}, "Invert function failed for an empty dictionary."


def test_invert_duplicate_values() -> None:
    """Test invert function with a dictionary containing duplicate values."""
    input_dict = {'a': 'apple', 'b': 'banana', 'c': 'apple'}
    with pytest.raises(KeyError, match="Duplicate value 'apple' encountered"):
        invert(input_dict)


def alphabetizer(words: List[str]) -> Dict[str, List[str]]:
    """Categorize words by the first letter."""
    alphabet_dict = {}
    for word in words:
        # Convert the word to lowercase to ensure consistent categorization
        word = word.lower()
        first_letter = word[0]
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def test_alphabetizer_normal_case() -> None:
    """Test alphabetizer function with a normal use case."""
    input_words = ["cat", "apple", "boy", "angry", "bad", "car"]
    result = alphabetizer(input_words)
    expected_result = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert result == expected_result, "Alphabetizer function failed for normal case."


def test_alphabetizer_empty_list() -> None:
    """Test alphabetizer function with an empty list."""
    input_words = []
    result = alphabetizer(input_words)
    assert result == {}, "Alphabetizer function failed for an empty list."


def test_alphabetizer_case_insensitivity() -> None:
    """Test alphabetizer function with case-insensitive input."""
    input_words = ["Cat", "Apple", "boy", "angry", "Bad", "Car"]
    result = alphabetizer(input_words)
    expected_result = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert result == expected_result, "Alphabetizer function failed for case-insensitive input."


def favorite_color(name_color_dict: Dict[str, str]) -> str:
    """Find the most popular color among a group of people."""
    color_count: Dict[str, int] = {}
    
    for name, color in name_color_dict.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    most_popular_color = max(color_count, key=color_count.get, default=None)
    
    return most_popular_color


def test_favorite_color_normal_case() -> None:
    """Test favorite_color function with a normal use case."""
    input_data = {'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue', 'David': 'red'}
    result = favorite_color(input_data)
    assert result == 'blue', "Favorite_color function failed for normal case."


def test_favorite_color_empty_dict() -> None:
    """Test favorite_color function with an empty dictionary."""
    input_data = {}
    result = favorite_color(input_data)
    assert result is None, "Favorite_color function failed for an empty dictionary."


def test_favorite_color_tiebreaker() -> None:
    """Test favorite_color function with a tiebreaker scenario."""
    input_data = {'Alice': 'red', 'Bob': 'blue', 'Charlie': 'green', 'David': 'blue'}
    result = favorite_color(input_data)
    assert result == 'blue', "Favorite_color function failed for a tiebreaker scenario."


def count(values: List[str]) -> Dict[str, int]:
    """Count the occurrences of each value in a list."""
    count_dict = {}
    for item in values:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def test_count_normal_case() -> None:
    """Test count function with a normal use case."""
    input_values = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    result = count(input_values)
    expected_result = {'apple': 3, 'banana': 2, 'cherry': 1}
    assert result == expected_result, "Count function failed for normal case."


def test_count_empty_list() -> None:
    """Test count function with an empty list."""
    input_values = []
    result = count(input_values)
    assert result == {}, "Count function failed for an empty list."


def test_count_case_insensitivity() -> None:
    """Test count function with case-insensitive input."""
    input_values = ["Apple", "Banana", "apple", "Cherry", "banana", "Apple"]
    result = count(input_values)
    expected_result = {'apple': 3, 'banana': 2, 'cherry': 1}
    assert result == expected_result, "Count function failed for case-insensitive input."


def update_attendance(attendance_dict: Dict[str, List[str]], day: str, student: str) -> Dict[str, List[str]]:
    """Update attendance."""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict


def test_update_attendance_normal_case() -> None:
    """Test update_attendance function with a normal use case."""
    input_attendance = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie']}
    result = update_attendance(input_attendance, 'Monday', 'David')
    expected_result = {'Monday': ['Alice', 'Bob', 'David'], 'Tuesday': ['Charlie']}
    assert result == expected_result, "Update_attendance function failed for normal case."


def test_update_attendance_empty_dict() -> None:
    """Test update_attendance function with an empty dictionary."""
    input_attendance = {}
    result = update_attendance(input_attendance, 'Wednesday', 'Eve')
    expected_result = {'Wednesday': ['Eve']}
    assert result == expected_result, "Update_attendance function failed for an empty dictionary."

def test_update_attendance_existing_day() -> None:
    """Test update_attendance function with an existing day."""
    input_attendance = {'Thursday': ['Frank', 'Grace']}
    result = update_attendance(input_attendance, 'Thursday', 'Hank')
    expected_result = {'Thursday': ['Frank', 'Grace', 'Hank']}
    assert result == expected_result, "Update_attendance function failed for an existing day."