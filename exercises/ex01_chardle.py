"""Ex01 - Chardle"""
    
__author__="730494174"

chosen_word: str = input("Enter a 5-character word: ")
if len(chosen_word) !=5:
    print("Error: Word must contain 5 characters")
    exit()
chosen_letter: str = input("Enter a single character: ")
if len(chosen_letter) !=1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + chosen_word)

pos_0 = (chosen_word[0])
pos_1 = (chosen_word[1])
pos_2 = (chosen_word[2])
pos_3 = (chosen_word[3])
pos_4 = (chosen_word[4])

instance: int = 0

if pos_0 == chosen_letter:
    print(chosen_letter + " found at index 0 ")
    instance = instance + 1
if pos_1 == chosen_letter :
    print(chosen_letter + " found at index 1 ")
    instance = instance + 1
if pos_2 == chosen_letter :
    print(chosen_letter + " found at index 2 ")
    instance = instance + 1
if pos_3 == chosen_letter :
    print(chosen_letter + " found at index 3 ")
    instance = instance + 1
if pos_4 == chosen_letter :
    print(chosen_letter + " found at index 4 ")
    instance = instance + 1


if instance == 0:
    print("No instances of " + chosen_letter + " found in " + chosen_word)
if instance == 1:
    print("1 instance of " + chosen_letter + " found in " + chosen_word)
else: 
    print(str(instance) + " instances of " + chosen_letter + " found in " + chosen_word)