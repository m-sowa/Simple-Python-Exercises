#Program calculates the Fibonacci number for the sequence position provided by the user.

#introduction
print("The Fibonacci sequence is a sequence in which each number is the sum of the two preceding numbers.")
print()

#asking for sequence element
n = int(input("Which number from the sequence would you like to see? "))

#calculating the Fibonacci number for that element
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    f0 = 0
    f1 = 1
    for i in range(0, n - 2):
        fibo = f0 + f1
        f0 = f1
        f1 = fibo
    print("Sequence element number", n, "equals", fibo)

#ending
input("\n\nPress Enter to finish.")