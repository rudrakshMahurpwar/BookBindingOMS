from modules.order_manager import OrderManager


def main():
    # Initialize the orders.csv file
    OrderManager.initialize_order_file()

    while True:
        print("\n📚 Book Binding Order Management System 📚")
        print("1️⃣ Create New Order")
        print("2️⃣ Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            # Process a new order (take input and save it)
            OrderManager.process_order()

        elif choice == "2":
            print("👋 Exiting... Have a great day!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
