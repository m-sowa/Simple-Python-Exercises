#Program provides the length of the string given by the user, lists all its vowels, and rewrites the string without vowels.

#introduction
print("Let's have some fun with a piece of text!")
print()

#asking for text
message = input("Write your text here: ")

#calculating the length of the text
print("\nThe number of characters in your text is:", len(message))

#listing and counting vowels
vowels = "aeiouy"
vowels_in_message = []

print("\nVowels used in your text: ", end="")
for letter in message:
    if letter.lower() in vowels:
        print(letter.lower(), end = " ")
        vowels_in_message.append(letter)

print("\n\nThe number of vowels in your text is:", len(vowels_in_message))

#rewriting the text without vowels
new_message = " "

for letter in message:
    if letter.lower() not in vowels:
        new_message += letter

print("\nHere's your text without any vowels in it:", new_message)

#ending
input("\n\nPress Enter to finish.")