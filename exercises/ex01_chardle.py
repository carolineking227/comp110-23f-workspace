"""Ex01 - Chardle."""
    
__author__ = "730494174"

chosen_word = input("Enter a 5-character word: ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chosen_letter = input("Enter a single character: ")
if len(chosen_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + chosen_letter + " in " + chosen_word)

count = 0

for i in range(len(chosen_word)):
    if chosen_word[i] == chosen_letter:
        print(f"{chosen_letter} found at index {i}")
        count += 1

if count == 0:
    print("No instances of " + chosen_letter + " found in " + chosen_word)
elif count == 1:
    print("1 instance of " + chosen_letter + " found in " + chosen_word)
else:
    print(f"{count} instances of {chosen_letter} found in {chosen_word}")
