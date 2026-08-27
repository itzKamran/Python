# Q. Find Largest and Smallest Without Built-ins
numbers = [45, 12, 89, 33, 7, 98, 23]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)
