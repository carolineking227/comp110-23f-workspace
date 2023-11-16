"""Test my zip function!"""
__author__ = 730494174

from lessons.zip import zip


def test_int_and_str_equal() -> None:
    """Test the zip of empty lists!"""
    test_str_list: list[int] = []
    test_int_list: list[int] = []
    assert zip(test_str_list, test_int_list) == {}


def test_use_case_one() -> None:
    """Test zip of lists with same length!"""
    test_str_list = ["pink", "blue", "purple"]
    test_int_list = [1, 2, 3]
    assert zip(test_str_list, test_int_list) == {"pink": 1, "blue": 2, "purple": 3}


def test_use_case_two() -> None: 
    """Test zip function with lists of different lengths!"""
    test_str_list = ["pink", "blue", "purple"]
    test_int_list = [1, 2, 3, 4]
    assert zip(test_str_list, test_int_list) == {}