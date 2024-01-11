#Program guesses the number given by the user. Attempts are counted.
#Program gets hints.

import random

#introduction
print("\n\tWelcome to the game!")
print("\nThe program has to guess your number. It will even get hints!")
number = int(input("\nNumber to be guessed (between 1-20): "))

#initializing variables
compMin = 1
compMax = 20
tries = 1

#program tries to "guess" the number
while True:
    print("\nGuessing within the range:", compMin, "-", compMax)
    guess = random.randint(compMin, compMax)
    print("Guess:", guess)

    if guess == number:
        print("\tWell done, computer!")
        break
    elif guess > number:
        print("\tToo high...")
        compMax = guess - 1
        tries += 1
    elif guess < number:
        print("\tToo low...")
        compMin = guess + 1
        tries += 1

#counting the number of attempts
print("\nNumber of attempts:", tries)

#ending
input("\n\nPress Enter to finish.")