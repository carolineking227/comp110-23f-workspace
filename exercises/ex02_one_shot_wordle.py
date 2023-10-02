"""Ex02- one shot wordle"""
    
__author__="730494174"

correct_answer: str = "python"
correct_answer_len: int = len(correct_answer)
guess: str = input("What is your 6-letter guess? ")

#variables
i: int = 0 
guess_boxes: str = ""
new_counter: int = 0
alt_ind: int = 0
wrong_place: bool = False

#coded boxes for printing
WHITE_BOX: str ="\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(correct_answer):
     guess = input("That was not 6-letters! Try again: ")

while i < len(correct_answer): 
   if guess[i] == correct_answer[i]:
        guess_boxes: str = guess_boxes + GREEN_BOX
        GREEN_BOX: str = "\U0001F7E9"
        i += 1
   elif guess[i] == correct_answer[alt_ind]:
             wrong_place = True
             guess_boxes: str = guess_boxes + YELLOW_BOX
   else: 
         guess_boxes: str = guess_boxes + WHITE_BOX
         i += 1
         WHITE_BOX: str = "\U00002B1C"
while wrong_place == False and i < len(correct_answer):
        if guess[i] == correct_answer[alt_ind]:
             wrong_place = True
             guess_boxes: str = guess_boxes + YELLOW_BOX
        else:
             alt_ind += 1
        
#print information 
if guess == correct_answer:
   print(guess_boxes)
   print("Woo! You got it! ")
else:
    print(guess_boxes)
    print("Not quite. Play again soon! ")