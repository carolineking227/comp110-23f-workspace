"""Practicing dictionary functions!"""
__author__ = 730494174


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Define invert and make sure it will raise a KeyError when needed!"""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError(f"KeyError: Duplicate value '{value}' encountered")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(name_color_dict: dict[str, str]) -> str:
    """Define favorite_color and ensure it returns the most popular color."""
    color_count: dict[str, int] = {}  # Create a dictionary to count the occurrences of each color
    color_order: dict[str, int] = {}  # Create a dictionary to store the order in which colors appear

    for name, color in name_color_dict.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        if color not in color_order:
            color_order[color] = len(color_order)

    def popularity_key(color: str):
        return (color_count[color], -color_order[color])

    most_popular_color = max(color_count, key=popularity_key)

    return most_popular_color


def count(values: list[str]) -> dict[str, int]:
    """Define count and return resulting dictionary."""
    count_dict: dict[str, int] = {}
    for item in values:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


result = count(["apple", "banana", "apple", "cherry", "banana", "apple"])
print(result)


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Define alphabetizer and return the letters and words belonging to each letter."""
    alphabet_dict: dict[str, list[str]] = {}  # Create an empty dictionary to store words categorized by the first letter

    for word in words:
        # Convert the word to lowercase to ensure consistent categorization
        word = word.lower()
        
        first_letter = word[0]
        
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]

    return alphabet_dict


result = alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"])
print(result)


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update attendance!"""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict