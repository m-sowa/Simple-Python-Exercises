#Program encrypts a message given by the user using Caesar's cipher

#introduction
print("This program will encrypt your message using the Caesar's cipher.")
print()

#asking for message and converting it to uppercase
plaintext = input("Write the message to be encrypted: ")
plaintext = plaintext.upper().strip()

#asking to specify the offset (shift)
offset = int(input("\nSpecify the offset (number of characters to shift by): "))

#encrypting the message - shifting by the offset provided (case for letters and for other Unicode characters)
ciphertext = ""
for letter in plaintext:
    if letter.isalpha():
        if letter == 'Z':
            letter = 'A'
        else:
            letter = chr(ord(letter) + offset)
    ciphertext += letter

print("\nThe encrypted message is:", ciphertext)

#ending
input("\n\nPress Enter to finish.")
