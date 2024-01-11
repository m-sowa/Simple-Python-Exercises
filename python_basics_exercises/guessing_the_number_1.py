#Program generates a random number in range 1-15. 
#User gets tips and has 4 attempts to guess the number.

import random

#introduction
print("Let's play a guessing game! What number between 1-15 do I have in mind?")

number = random.randint(1, 15)

tries = 4

for i in range(1, tries+1):
    guess = int(input("\nYour guess: "))

    if guess == number:
        print("Well done!")
        break
    elif guess > number:
        print("Too high...")
    else:
        print("Too low...")
        
    if tries-i == 0:
        print("\nNo luck, game over! The number was:", number)
    else:
        print("Attempts left:", tries-i)

#ending
input("\n\nPress Enter to finish.")