#Program sorts numbers given by the user

#introduction
print("Hey there! Give me three numbers and I'll sort them.")
a = int(input("\nFirst number: "))
b = int(input("\nSecond number: "))
c = int(input("\nThird number: "))

#sorting the numbers
print("\nHere's your sorted list: ", end ="")
if a < b and a < c:
    print(a, end=" ")
    if b < c:
        print(b, c)
    else:
        print(c, b)
elif b < a and b < c:
    print(b, end=" ")
    if a < c:
        print(a, c)
    else:
        print(c, a)
else:
    print(c, end=" ")
    if a < b:
        print(a, b)
    else:
        print(b, a)

#ending
input("\n\nPress Enter to finish.")