menu = {
     "Pizza": 120,
    "Burger": 59,
    "Fries": 65,
    "Pasta": 50,
    "Salad": 40,
    "Sandwich": 79,
    "Soup": 80,
    "Taco": 99,
    "Ice Cream": 30,
    "Coffee": 99

}

order = {} # {item_name: quantity}

def display_menu():
    print("\n--- MENU ---")
    print("Item Name | Price")
    print("----------------|------")
    for item, price in menu.items():
        print(f"{item:<15} | ₹{price}")
    print()

def add_to_order():
    display_menu()
    print("Enter items to add. Type 'done' when finished.")

    while True:
        item = input("\nEnter item name or 'done': ").title()

        if item.lower() == 'done':
            print("Finished adding items.")
            break

        if item not in menu:
            print("Item not available in menu. Try again.")
            continue

        try:
            qty = int(input(f"Enter quantity for {item}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Invalid quantity. Enter a number.")
            continue

        if item in order:
            print(f"{item} already in order with quantity {order[item]}.")
            choice = input("Type 'add' to add more or 'update' to replace quantity: ").lower()

            if choice == 'add':
                order[item] += qty
                print(f"Updated: {order[item]} x {item} in order.")
            elif choice == 'update':
                order[item] = qty
                print(f"Updated: {qty} x {item} in order.")
            else:
                print("Invalid choice. Item not changed.")
        else:
            order[item] = qty
            print(f"{qty} x {item} added to order.")

def remove_from_order():
    if not order:
        print("Order is empty.")
        return

    view_order()
    item = input("Enter item name to remove: ").title()
    if item in order:
        del order[item]
        print(f"{item} removed from order.")
    else:
        print("Item not in your order.")

def view_order():
    if not order:
        print("Your order is empty.")
        return

    print("\n--- CURRENT ORDER ---")
    print("Item Name | Qty | Price | Total")
    print("----------------|-----|-------|------")
    for item, qty in order.items():
        price = menu[item]
        total = price * qty
        print(f"{item:<15} | {qty:^3} | ₹{price:<4} | ₹{total}")
    print()

def generate_bill():
    if not order:
        print("Your order is empty. Add items first.")
        return

    print("\n========= FINAL BILL =========")
    print("Item Name | Qty | Price | Total")
    print("----------------|-----|-------|------")

    subtotal = 0
    for item, qty in order.items():
        price = menu[item]
        total = price * qty
        subtotal += total
        print(f"{item:<15} | {qty:^3} | ₹{price:<4} | ₹{total}")

    print("----------------|-----|-------|------")
    print(f"Subtotal: ₹{subtotal}")

    # Discount Rules: 10% if >500, 15% if >1000
    discount = 0
    if subtotal > 1000:
        discount = subtotal * 0.15
        print(f"Discount 15%: -₹{discount:.2f}")
    elif subtotal > 500:
        discount = subtotal * 0.10
        print(f"Discount 10%: -₹{discount:.2f}")
    else:
        print("Discount: ₹0")

    final_amount = subtotal - discount
    print("-------------------------------")
    print(f"Final Payable Amount: ₹{final_amount:.2f}")
    print("===============================")

    order.clear() # Reset order after billing

def add_menu_item():
    item = input("Enter new food item name: ").title()
    if item in menu:
        print("Item already exists in menu.")
        return
    try:
        price = int(input("Enter price: ₹"))
        if price <= 0:
            print("Price must be greater than 0.")
            return
        menu[item] = price
        print(f"{item} added to menu at ₹{price}.")
    except ValueError:
        print("Invalid price. Enter a number.")

def main():
    while True:
        print("\n=== Online Food Ordering System ===")
        print("1. Display Menu")
        print("2. Add Items to Order")
        print("3. Remove Item from Order")
        print("4. View Current Order")
        print("5. Generate Final Bill")
        print("6. Add New Item to Menu")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            add_to_order()
        elif choice == "3":
            remove_from_order()
        elif choice == "4":
            view_order()
        elif choice == "5":
            generate_bill()
        elif choice == "6":
            add_menu_item()
        elif choice == "7":
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid choice. Enter 1-7.")

if __name__ == "__main__":
    main()
