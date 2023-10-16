"""practice with list utility functions"""

__author__ = "730494174"

def all(nums, target):
    # Check if the list is empty
    if not nums:
        return False

    for num in nums:
        if num != target:
            return False

    return True


def max(input):
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max_num = input[0]

    for num in input:
        if num > max_num:
            max_num = num

    return max_num


def is_equal(list1, list2):
    # Checks list length
    if len(list1) != len(list2):
        return False

    # Compares each place in the lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True