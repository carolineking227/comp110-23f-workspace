"""Wordle restricted to 6 guesses."""

__author__ = "730494174"

#contains_char function - checks for letter presence
def contains_char(wordle: str, letter: str) -> bool:
    assert len(letter) == 1
    i_yellow: int = 0
    while i_yellow < len(wordle):
        if letter == wordle[i_yellow]:
            return True
        i_yellow += 1
    return False

#emojified function - shows you with emojis if your letter is in the word, and if it is placed correctly
def emojified(guess: str, wordle: str) -> str:
    assert len(guess) == len(wordle)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_boxes_str: str = ""
    while i < len(wordle):
        if guess[i] == wordle[i]:
            emoji_boxes_str += GREEN_BOX
        elif contains_char(wordle, guess[i]) is True:
            emoji_boxes_str += YELLOW_BOX
        else:
            emoji_boxes_str += WHITE_BOX
        i += 1
    return emoji_boxes_str   

#input_guess function - ensures guess length matches wordle length
def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess 

#main function - defined variables and a while loop for the winning/losing status of the game
def main() -> None:
    """The entrypoint of the program and the game loop."""
    wordle: str = "codes"
    expected_length: int = len(wordle)
    turn_status: int = 1
    turn_str: str = ""
    win_status: bool = False
    # these are variables exclusive to the game loop and aren't used in any of the other three defined functions.

    while turn_status <= 6 and win_status is False:
        emoji_boxes_str: str = ""
        guess: str = ""
        turn_str = f"=== Turn {turn_status}/6 ==="
        print(turn_str)
        guess += input_guess(expected_length)
        emoji_boxes_str += emojified(guess, wordle)
        print(emoji_boxes_str)
        if guess == wordle:
            win_status = True
        else:
            turn_status += 1
    
    #printed information
    if win_status is True:
        print(f"You won in {turn_status}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

#this makes it possible to fun Python program as a module and for other modules to import the functions for reuse.
if __name__ == "__main__":
    main()