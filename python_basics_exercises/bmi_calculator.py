#Program calculates BMI based on data provided by the user.

#defining function to calculate bmi
def bmi(weight, height):
    return weight / (height**2)

#defining function to determine bmi category
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight."
    elif bmi >= 18.5 and bmi < 25:
        return "normal weight."
    elif bmi >= 25 and bmi < 30:
        return "noverweight."
    else:
        return "obesity."

#getting user input and checking for validity
input_weight = input("\nHow much do you weight? (kg): ")

if not input_weight.isnumeric():
    print("This is not a valid number!")
    exit()

weight = float(input_weight)

input_height = input("\nHow tall are you? (cm): ")

if not input_height.isnumeric():
    print("This is not a valid number!")
    exit()

height = float(input_height)/100

#calculating bmi and determining bmi category
bmi_result = round(bmi(weight, height), 2)

print("\n\tYour BMI is:", bmi_result, "kg/m\u00b2")
print("\tThis is considered", bmi_category(bmi_result))

#ending
input("\n\nPress Enter to finish.")