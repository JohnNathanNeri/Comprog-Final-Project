# Shopping Cart System with Predefined Items and Prices

# Predefined list of items and their prices
available_items = [
    {"name": "Apple", "price": 1.00},
    {"name": "Banana", "price": 0.50},
    {"name": "Orange", "price": 0.75},
    {"name": "Milk", "price": 2.50},
    {"name": "Bread", "price": 1.50}
]

# List to store items added to the cart
shopping_cart = []

# Function to display available items
def display_available_items():
    print("\nAvailable Items:")
    for i, item in enumerate(available_items, 1):
        print(f"{i}. {item['name']} - ${item['price']}")

# Function to display the cart
def display_cart():
    if not shopping_cart:
        print("\nYour cart is empty.")
    else:
        print("\nItems in your cart:")
        total = 0
        for i, item in enumerate(shopping_cart, 1):
            print(f"{i}. {item['name']} - ${item['price']}")
            total += item["price"]
        print(f"\nTotal Price: ${total}")
        return total

# Function to add an item to the cart
def add_item():
    while True:
        display_available_items()
        choice = input("\nEnter the number of the item to add to your cart (or type 'back' to return to the menu): ")
        if choice.lower() == "back":
            print("Returning to the main menu...")
            break
        item_index = int(choice) - 1  # Convert to 0-based index
        if 0 <= item_index < len(available_items):
            selected_item = available_items[item_index]
            shopping_cart.append(selected_item)
            print(f"'{selected_item['name']}' has been added to your cart.")
        else:
            print("Invalid choice. Please select a valid item number.")

# Function to remove an item from the cart
def remove_item():
    if not shopping_cart:
        print("\nYour cart is empty. Nothing to remove.")
        return
    display_cart()
    item_number = int(input("\nEnter the number of the item to remove: "))
    if 1 <= item_number <= len(shopping_cart):
        removed_item = shopping_cart.pop(item_number - 1)
        print(f"'{removed_item['name']}' has been removed from your cart.")
    else:
        print("Invalid item number.")

# Function to checkout with payment validation
def checkout():
    if not shopping_cart:
        print("\nYour cart is empty. Add some items before checking out.")
    else:
        total = display_cart()  # Display the cart and calculate total
        while True:
            amount_paid = float(input(f"\nYour total is ${total}. Please enter the amount you wish to pay: $"))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"\nThank you for your payment of ${amount_paid}.")
                if change > 0:
                    print(f"Your change is: ${change}.")
                shopping_cart.clear()  # Clear the cart after successful checkout
                print("Thank you for shopping with us!")
                break
            else:
                print("Insufficient amount. Please enter a payment that is greater than or equal to the total amount.")

# Main menu function
def shopping_cart_menu():
    while True:
        print("\nShopping Cart Menu:")
        print("1. View Cart")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        # Get user choice
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

# Run the shopping cart system
shopping_cart_menu()
