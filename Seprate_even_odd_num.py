# Separate Even and Odd Numbers
numbers = []

for i in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

even_list = []
odd_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print("Original list:", numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
