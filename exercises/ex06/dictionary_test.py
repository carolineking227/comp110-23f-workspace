"""EX07 dict unit tests!"""
__author__ = 730494174

import unittest
import pytest
from exercises import invert, favorite_color, count, alphabetizer, update_attendance


class TestFunctions(unittest.TestCase):
    """Creating a class to test the following functions!"""

    def test_invert_expected_use_case(self):
        """Testing expected invert!"""
        input_dict = {"a": "apple", "b": "banana", "c": "cherry"}
        expected_output = {"apple": "a", "banana": "b", "cherry": "c"}
        self.assertEqual(invert(input_dict), expected_output)

    def test_invert_edge_case(self):
        """Testing invert!"""
        input_dict = {"a": "apple", "b": "banana", "c": "apple"}
        with self.assertRaises(KeyError):
            invert(input_dict)

    def test_favorite_color_expected_use_case(self):
        """Testing expected favorite color!"""
        name_color_dict = {"John": "blue", "Alice": "red", "Bob": "blue", "Eve": "green"}
        expected_output = "blue"
        self.assertEqual(favorite_color(name_color_dict), expected_output)

    def test_favorite_color_edge_case(self):
        """Testing favorite color!"""
        name_color_dict = {}
        expected_output = None  # There are no colors, so it should return None
        self.assertEqual(favorite_color(name_color_dict), expected_output)
    
    def test_count_expected_use_case(self):
        """Testing expected count!"""
        values = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        expected_output = {"apple": 3, "banana": 2, "cherry": 1}
        self.assertEqual(count(values), expected_output)

    def test_count_edge_case(self):
        """Testing count!"""
        values = []
        expected_output = {}
        self.assertEqual(count(values), expected_output)

    def test_alphabetizer_expected_use_case(self):
        """Testing expected alphabetizer!"""
        words = ["cat", "apple", "Bat", "apply", "bad", "car"]
        expected_output = {
            "a": ["apple", "apply"],
            "b": ["bad"],
            "B": ["Bat"],
            "c": ["cat", "car"]
        }
        self.assertEqual(alphabetizer(words), expected_output)

    def test_alphabetizer_edge_case(self):
        """Testing alphabetizer!"""
        words = []
        expected_output = {}
        self.assertEqual(alphabetizer(words), expected_output)

    def test_update_attendance_expected_use_case(self):
        """Testing expected update attendance!"""
        attendance_dict = {"Monday": ["Alice", "Bob"], "Tuesday": ["Alice"]}
        day = "Tuesday"
        student = "Eve"
        expected_output = {"Monday": ["Alice", "Bob"], "Tuesday": ["Alice", "Eve"]}
        self.assertEqual(update_attendance(attendance_dict, day, student), expected_output)

    def test_update_attendance_edge_case(self):
        """Testing update attendance!"""
        attendance_dict = {}
        day = "Wednesday"
        student = "Alice"
        expected_output = {"Wednesday": ["Alice"]}
        self.assertEqual(update_attendance(attendance_dict, day, student), expected_output)

    def test_invert_key_error():
        """Testing for KeyError!"""
        with pytest.raises(KeyError):
            input_dict = {'apple': 'banana', 'carrot': 'banana'}
            invert(input_dict)


if __name__ == '__main__':
    unittest.main()