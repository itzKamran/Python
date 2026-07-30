def process_string(word, user_index=None):
    # 1. Display length of string
    print("Length of String :", len(word))

    # 2. Display first and last character safely
    if word:
        print(f"First index Char : '{word[0]}', Last index Char : '{word[-1]}'")

    # 3. Uppercase, Lowercase, and Capitalize conversions
    upper_case = word.upper()
    lower_case = word.lower()
    capitalize = word.capitalize()

    # 4. Check character at the given index if provided
    if user_index is not None:
        try:
            idx = int(user_index)
            print(f"Character at index {idx} : '{word[idx]}'")
        except IndexError:
            print(f"Index {user_index} is out of bounds for string of length {len(word)}.")
        except ValueError:
            print("Please enter a valid integer for index.")

    return upper_case, lower_case, capitalize


# --- Main Execution ---
my_word = "Kamran Siddique"

# Ask user for an index input
idx_input = input("Enter a string index to check character: ")

# Run function
upper, lower, cap = process_string(my_word, idx_input)

print("\nResults:")
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Capitalized:", cap)

"""
Enter a string index to check character: Kamran Siddique - input
Length of String : 15
First index Char : 'K', Last index Char : 'e'
Please enter a valid integer for index.

Results:
Uppercase: KAMRAN SIDDIQUE
Lowercase: kamran siddique
Capitalized: Kamran siddique

"""


