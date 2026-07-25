attendance = {}

while True:
    print("\n1.Mark Attendance")
    print("2.View Attendance")
    print("3.Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        name = input("Student Name: ")
        status = input("Present/Absent: ")
        attendance[name] = status

    elif ch == 2:
        print(attendance)

    else:
        break
