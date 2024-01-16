# Vending machine items, prices, and stocks
drink_menu = {
    '1': {'name': 'Coke', 'price': 1.50, 'stock': 5},
    '2': {'name': 'Water', 'price': 1.00, 'stock': 8},
    '3': {'name': 'Orange Juice', 'price': 2.00, 'stock': 3}
}

snack_menu = {
    '4': {'name': 'Chips', 'price': 1.75, 'stock': 10},
    '5': {'name': 'Chocolate Bar', 'price': 1.25, 'stock': 7},
    '6': {'name': 'Granola Bar', 'price': 1.50, 'stock': 4}
}

def display_menu(menu):
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']} ({item['stock']} in stock)")

def make_purchase(menu):
    selection = input("Enter the item number you wish to purchase: ")

    if selection in menu:
        selected_item = menu[selection]
        item_type = 'drink' if menu is drink_menu else 'snack'
    else:
        print("Invalid selection. Please try again.")
        return None

    if selected_item['stock'] <= 0:
        print("Sorry, this item is out of stock. Please choose another item.")
        return None

    print(f"You have selected {selected_item['name']} ({item_type}).")
    amount_due = selected_item['price']

    while amount_due > 0:
        try:
            payment = float(input(f"Please insert ${amount_due:.2f}: "))
            if payment >= amount_due:
                change = payment - amount_due
                print(f"Thank you for your purchase! Your change is ${change:.2f}.")

                if item_type == 'drink':
                    print("Enjoy your drink! Would you like to try a snack?")
                elif item_type == 'snack':
                    print("Enjoy your snack! How about adding a drink next time?")

                # Update stock
                selected_item['stock'] -= 1
                return selected_item
            else:
                print("Insufficient payment. Please insert more money.")
                amount_due -= payment
        except ValueError:
            print("Invalid payment amount. Please enter a valid number.")

def buy_again():
    return input("Do you want to make another purchase? (yes/no): ").lower() == 'yes'

# Main program
while True:
    print("Welcome to the Vending Machine!")
    print("Drink Menu:")
    display_menu(drink_menu)
    print("\nSnack Menu:")
    display_menu(snack_menu)

    purchased_item = make_purchase(drink_menu) or make_purchase(snack_menu)

    if not purchased_item or not buy_again():
        print("Thank you for using the vending machine. Have a great day!")
        break