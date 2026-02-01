#Contact Management system

contacts = {}

while True:
    print("\n1.Add  2.View  3.Search  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        name = input("Search name: ")
        print(contacts.get(name, "Not Found"))

    elif choice == "4":
        break
