"""Program that loops until correct numnber is guessed"""

from random import randint

secret: int = randint(1,15)
guess: int = int(input("Guess a number between 1 and 15: "))
number_of_tries: int = 1
max_tries: int = 3

while (guess != secret) and (number_of_tries < max_tries):
    print("Wrong!")
    if (guess < 1) or (guess > 15):
        print("That's not between 1 and 15! ")
    if guess < secret: 
        print("Too low... ")
    else:
        print("Too high... ")
    guess = int(input("Guess again: "))
    number_of_tries += 1
if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose! :( ")