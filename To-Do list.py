#To-Do list

tasks = []

while True:
    print("\n1.Add Task  2.View Tasks  3.Remove Task  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == "3":
        num = int(input("Task number to remove: "))
        tasks.pop(num - 1)

    elif choice == "4":
        break
