#Program does a few operations on randomly generated numbers

#program generates 10 random numbers from range 1-100 and adds them to a list
import random
generated_list = []
tries = 0

while tries < 5:
    number = random.randint(1, 30)
    if number not in generated_list:
        generated_list.append(number)
        tries += 1

print("\nThe randomly generated numbers are:", generated_list)

#sorting numbers in ascending order:
generated_list.sort()
print("\nNumbers sorted in ascending order:", generated_list)

#sorting numbers in descending order:
generated_list.sort(reverse = True)
print("\nNumbers sorted in descending order:", generated_list)

#adding all the numbers:
total = 0
for i in generated_list:
    total += i

print("\nSum of all the numbers is:", total)

#finding the lowest number:
lowest = generated_list[0]
for i in generated_list:
    if i < lowest:
        lowest = i

print("\nThe lowest number is:", lowest)

#removing the highest number:
highest = generated_list[0]
for i in generated_list:
    if i > highest:
        highest = i

generated_list.remove(highest)
generated_list.sort()

print("\nThe list without the highest number:", generated_list)

#adding the product of the remaining numbers to the beginning of the list:
product = 1
for i in generated_list:
    product *= i

generated_list.insert(0, product)

print("\nThe list with the product of its numbers added at the front:", generated_list)

#ending
input("\n\nPress Enter to finish.")