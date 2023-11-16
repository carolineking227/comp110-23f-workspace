"""Combining two lists into a dictionary!"""
___author___ = 730494174


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Defining the function zip and returning empty list when str and int lists are inequal!"""
    if len(str_list) != len(int_list) or not str_list:
        return {}
    """When indexes match, return the result!"""
    result = {}
    for i in range(len(str_list)):
        result[str_list[i]] = int_list[i]
    
    return result