"""Ex02- one shot wordle."""
    
__author__ = "730494174"


secret_word = "python"
guess = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

ind = 0
result = ""

while ind < len(secret_word):
    if guess[ind] == secret_word[ind]:
        result += GREEN_BOX
    else:
        result += YELLOW_BOX
    ind += 1

ind = 0
while ind < len(secret_word):
    if guess[ind] != secret_word[ind]:
        wrong_place = False

        alt_index = 0

        while not wrong_place and alt_index < len(secret_word):
            if guess[ind] == secret_word[alt_index] and alt_index != ind:
                wrong_place = True
            else:
                alt_index += 1
                
if wrong_place:
        result += YELLOW_BOX
else: 
        result += WHITE_BOX

ind += 1

print(result)

if result.count(GREEN_BOX) == len(secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")