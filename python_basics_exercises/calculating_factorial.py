#Program calculates the factorial of a number given by the user

print("Let's find the factorial of your number")
n = int(input("\nWrite your number here: "))
factorial = 1

for i in range(0, n):
    factorial = factorial * (i + 1)

print("\nThe factorial of", n, "is", factorial)

#ending
input("\n\nPress Enter to finish.")