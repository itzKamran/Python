#find a second largest number

numbers = [10, 20, 4, 45, 99]
numbers = list(set(numbers))
numbers.sort()
print("Second largest:", numbers[-2])
