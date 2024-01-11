#Program generates a random prophecy

import random

#introduction
print("Hello! I'll be your oracle for today!")
print("\nToday you will...")

#generating a random number assigned to a prophecy
prophecy = random.randint(1, 5)

#przypisanie
if prophecy == 1:
    print("\n...meet someone nice!")
elif prophecy == 2:
    print("\n...eat something delicious!")
elif prophecy == 3:
    print("\n...bump into someone unpleasant!")
elif prophecy == 4:
    print("\n...receive an important message!")
elif prophecy == 5:
    print("\n...have a wonderful day!")

#ending
input("\n\nPress Enter to finish.")