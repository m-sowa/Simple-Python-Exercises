#Programs find the highest number from a fixed-length list

#introduction
print("Give me five numbers and I'll tell you which one is the highest!")
print()

#starting with an empty list
values = []

#filling the list with 5 values given by the user
for i in range(5):
    number = int(input("Give a number: "))
    if number not in values:
        values.append(number)

#finding max value from the list
highest = values[0]
for i in values:
    if i > highest:
        highest = i

print("\nLet's see... The highest number is", highest, "!")

#ending
input("\n\nPress Enter to finish.")