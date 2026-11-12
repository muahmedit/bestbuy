import products
import store


def start(store_obj):
    """Displays the main menu and handles user interaction for the store."""
    while True:
        print("\n--- Store Menu ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number (1-4): ").strip()

        if choice == "1":
            print("\n--- Available Products ---")
            # Assuming your Store class has a method to list or iterate products
            all_products = store_obj.get_all_products()
            for index, product in enumerate(all_products, start=1):
                print(f"{index}. {product}")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")

        elif choice == "3":
            print("\n--- Make an Order ---")
            # Implement order logic here (e.g., prompting for product and quantity)
            pass

        elif choice == "4":
            print("\nThank you for shopping with us. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


def main():
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    # Start the user interface loop
    start(best_buy)


if __name__ == "__main__":
    main()