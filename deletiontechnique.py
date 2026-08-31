# Deletion Techniques
items = ["Pen", "Pencil", "Eraser", "Scale", "Sharpener", "Notebook"]

print("Original list:", items)

# Remove Pencil
items.remove("Pencil")
print("After remove():", items)

# Remove element at index 2
removed_item = items.pop(2)
print("Removed item:", removed_item)
print("After pop():", items)

# Delete first element
del items[0]
print("After del:", items)

# Clear all elements
items.clear()
print("After clear():", items)
