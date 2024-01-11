#Program verifies the validity of a given PESEL number (https://en.wikipedia.org/wiki/PESEL)

#introduction
pesel = input("PESEL number for validation: ")
pesel = pesel.strip()

#formula for the check digit:
#c1·1 + c2·3 + c3·7 + c4·9 + c5·1 + c6·3 + c7·7 + c8·9 + c9·1 + c10·3 + c11·1

#checking if number is long enough & has digits only; if yes, validating the check digit
if len(pesel) != 11:
    print("\nIncorrect number of digits.")
elif not pesel.isdigit():
    print("\nOnly digits are allowed.")
else:
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    sum = 0
    for i in range(11):
        sum += multipliers[i] * int(pesel[i])
    if sum % 10 == 0:
        print("\nPESEL is valid.")
    else:
        print("\nPESEL is invalid.")

#ending
input("\n\nPress Enter to finish.")