#Program makes the computer guess a randomly generated number. 
#Program counts the number of attempts. Max 100 attempts. Guesses may repeat.

import random

#initializing variables
tries = 1
minNumber = 1
maxNumber = 20

#generating random number
number = random.randint(minNumber, maxNumber)
print("\nThe number to be guessed is:", number)

#computer tries to "guess" the number
while True:
    guess = random.randint(minNumber, maxNumber)
    print("\nGuess: ", guess)

    if number == guess:
        print("Well done, computer!")
        print("Attempts needed:", tries)
        break
    else:
        print("Wrong guess...")
        tries += 1
        
        #adding a limit of 100 tries
        if tries >= 100:
            print("\nGame over :-(")
            break

#ending
input("\n\nPress Enter to finish.")