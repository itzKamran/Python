def sum_list(numbers):
    # Base case: an empty list sums to 0
    if not numbers:
        return 0
    
    # Recursive step: head (first element) + sum of tail (rest of the elements)
    return numbers[0] + sum_list(numbers[1:])

# --- Testing the recursive sum ---
my_numbers = [10, 20, 30, 40]

result = sum_list(my_numbers)

print("Sum:", result) # 100
print("Original intact:", my_numbers) # [10, 20, 30, 40]
