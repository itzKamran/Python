marks = []

while True:

    print("\n===== Student Marks Manager =====")
    print("1. Add a new mark")
    print("2. Insert a mark")
    print("3. Remove a mark")
    print("4. Display sorted marks")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        mark = int(input("Enter mark: "))
        marks.append(mark)

        print("Mark added successfully.")
        print("Marks:", marks)

    elif choice == 2:

        mark = int(input("Enter mark: "))
        position = int(input("Enter position: "))

        marks.insert(position, mark)

        print("Mark inserted successfully.")
        print("Marks:", marks)

    elif choice == 3:

        mark = int(input("Enter mark to remove: "))

        if mark in marks:
            marks.remove(mark)
            print("Mark removed successfully.")
        else:
            print("Mark not found.")

        print("Marks:", marks)

    elif choice == 4:

        marks.sort()

        print("Sorted marks:", marks)

    elif choice == 5:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")
