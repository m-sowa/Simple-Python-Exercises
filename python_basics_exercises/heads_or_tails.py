#Program tosses a coin 10 times and gives the number of heads and tails.

#introduction
print("The program will toss the coin 10 times. Who do you think will win: heads or tails? ")
input("\nPress Enter to begin!")
print()

#number of tosses
toss = 0

#number of heads (0)
head = 0

#number of tails (1)
tail = 0

#program tosses the coin: 0 is heads, 1 is tail
import random

while True:
    face = random.randint(0, 1)
    toss += 1

    #counting the number of heads and tails
    if face == 0:
        print("toss", toss, ": head")
        head += 1
    else:
        print("toss", toss, ": tail")
        tail += 1
    
    #limit to the number of tosses
    if toss >= 10:
        break

#result    
print("\nNumber of heads: ", head)
print("Number of tails: ", tail)
print()

if head == tail:
    print("It's a DRAW!")
elif head > tail:
    print("HEADS win!")
else:
    print("TAILS win!")

#ending
input("\n\nPress Enter to finish.")