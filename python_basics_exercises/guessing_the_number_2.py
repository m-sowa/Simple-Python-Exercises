#Program generates a random number between 1-50. 
#User gets tips and has an unlimited number of guesses.
#Program shows the number of attempts that user needed to guess. 

import random

#introduction
print("\tWelcome to the game!")
print("\nI'm thinking of a number between 1 and 50.")
print("Try to guess the number in as few attempts as possible.")

#initiating variables
number = random.randint(1, 50)
guess = 0
tries = 1

#analyzing user's guesses
while True:
    guess = int(input("\nYour guess: "))
    if guess > number:
        print("Too high...")
    elif guess < number:
        print("Too low...")
    else:
        print("Well done! The number is", number, "!")
        break

    tries += 1

print("\nYou needed", tries, "attempts to guess my number.")

#ending
input("\n\nPress Enter to finish.")