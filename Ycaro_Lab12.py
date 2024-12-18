def display_menu():
    menu = {
        1: ("Sisig", 60.00),
        2: ("Adobo", 60.00),
        3: ("Sinigang", 60.00),
        4: ("Rice", 10.00),
        5: ("Softdrinks", 15.00)
    }
    print("\nMenu:")
    for item, details in menu.items():
        print(f"{item}. {details[0]} - P{details[1]:.2f}")
    return menu

def take_order(menu):
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if choice in menu:
                item_name, item_price = menu[choice]
                print(f"You selected: {item_name} (P{item_price:.2f})")
                return item_price
            else:
                print("Invalid. Please select an item from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nTotal cost is P{total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment success! Your change is P{change:.2f}.")
                break
            else:
                print(f"Insufficient payment. You need at least P{total_cost - cash:.2f} more.")
        except ValueError:
            print("Invalid. Please enter a valid amount.")

def main():
    print("Welcome to the Food Ordering System!")
    menu = display_menu()
    total_cost = take_order(menu)
    process_payment(total_cost)
    print("\nThank you for ordering! Enjoy your meal!")

if __name__ == "__main__":
    main()