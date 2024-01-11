#Program calculates the area of a rectangle based on sides given by user.

#introduction
print("Hello! Let's calculate the area of your rectangle.")

#asking for side a
while True:
    side_a = int(input("\nThe length of side a: "))
    if side_a > 0:
        break
    else:
        print("\nWhoah! The value must be positive...")

#asking for side b
while True:
    side_b = int(input("\nThe length of side b: "))
    if side_b > 0:
        break
    else:
        print("\nWhoah! The value must be positive...")

#calculating rectangle area
area = side_a * side_b
print("\nThe area of your rectangle is:", area)

#ending
input("\n\nPress Enter to finish.")