#Program checks if the figure whose area and one side is given by the user is a square or a rectangle.

#introduction
print("Let's check if your figure is a square or a rectangle!")
print()

#asking for the area and one side
area = int(input("Area of the figure: "))
side1 = int(input("Length of one of its sides: "))

#calculating the other side
side2 = area / side1

#checking if the figure is a square or a root
if side1 == side2:
    print("\nYour figure is a SQUARE.")
else:
    print("\nYour figure is a RECTANGLE.")

#ending
input("\n\nPress Enter to finish.")