available_items = [
    {"name": "Hotdog", "price": 100.00},
    {"name": "Phone", "price": 200.50},
    {"name": "Pencil", "price": 50.75},
    {"name": "Shirt", "price": 89.50},
    {"name": "Keyboard", "price": 999.50}
]

shopping_cart = []

def display_available_items():
    print("\nAvailable Items:")
    item_number = 1
    for item in available_items:
        print(f"{item_number}. {item['name']} - ${item['price']}")
        item_number += 1

def display_cart():
    if len(shopping_cart) == 0:
        print("\nYour cart is empty.")
    else:
        print("\nItems in your cart:")
        total = 0
        item_number = 1
        for item in shopping_cart:
            print(f"{item_number}. {item['name']} - ${item['price']}")
            total += item["price"]
            item_number += 1
        print(f"\nTotal Price: ${total}")
        return total

def add_item():
    while True:
        display_available_items()
        choice = input("\nEnter the number of the item to add to your cart (or type 'back' to return to the menu): ")
        if choice.lower() == "back":
            print("Returning to the main menu...")
            break
        item_index = int(choice) - 1 
        if 0 <= item_index < len(available_items):
            selected_item = available_items[item_index]
            shopping_cart.append(selected_item)
            print(f"'{selected_item['name']}' has been added to your cart.")
        else:
            print("Invalid choice. Please select a valid item number.")

def remove_item():
    if len(shopping_cart) == 0:
        print("\nYour cart is empty. Nothing to remove.")
    else:
        display_cart()
        item_number = int(input("\nEnter the number of the item to remove: "))
        if 1 <= item_number <= len(shopping_cart):
            removed_item = shopping_cart.pop(item_number - 1)
            print(f"'{removed_item['name']}' has been removed from your cart.")
        else:
            print("Invalid item number.")

def checkout():
    if len(shopping_cart) == 0:
        print("\nYour cart is empty. Add some items before checking out.")
    else:
        total = display_cart() 
        while True:
            amount_paid = float(input(f"\nYour total is ${total}. Please enter the amount you wish to pay: $"))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"\nThank you for your payment of ${amount_paid}.")
                if change > 0:
                    print(f"Your change is: ${change}.")
                shopping_cart.clear()
                print("Thank you for shopping with us!")
                break
            else:
                print("Insufficient amount. Please enter a payment that is greater than or equal to the total amount.")

def shopping_cart_menu():
    while True:
        print("\nShopping Cart Menu:")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_cart()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Thank you for using the Shopping Cart System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

shopping_cart_menu()
