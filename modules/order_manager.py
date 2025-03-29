import sys
import os


# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from modules.order_input import OrderInput  # Updated import
from modules.order_saver import OrderSaver  # Updated import
from config import ORDER_FILE, ORDER_FIELDS  # Updated import

# Define the path for storing order data
ORDER_FILE = os.path.join("data", "orders.csv")

# Define the order fields
ORDER_FIELDS: list[str] = [
    "Order ID",
    "Customer Name",
    "Order Type",
    "Books Count",
    "Black & White Prints",
    "Color Prints",
    "OHP Sheets",
    "Expected Delivery",
    "Order Status",
    "Total Price",
]


class OrderManager:
    """Manages the overall order process, including initialization, input, and saving."""

    @staticmethod
    def initialize_order_file() -> None:
        """
        Ensures the orders.csv file exists and has the correct header row.
        """
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(ORDER_FILE):
            with open(ORDER_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=ORDER_FIELDS)
                writer.writeheader()
            print(f"✅ Initialized {ORDER_FILE} with headers.")
        else:
            print(f"ℹ {ORDER_FILE} already exists.")

    @staticmethod
    def process_order() -> None:
        """
        Takes the order data from the user using OrderInput, displays the details,
        and saves it to the orders.csv file using OrderSaver if confirmed.
        """
        while True:
            # Step 1: Take order details from the user
            order_data: dict = OrderInput.take_order()

            # Step 2: Calculate additional details
            binding_cost = order_data["Books Count"] * 50.0  # Cost for binding one book
            ohp_cost = order_data["OHP Sheets"] * 2.00  # Cost per OHP sheet
            bw_print_cost = (
                order_data["Black & White Prints"] * 0.10
            )  # Cost per black & white print
            color_print_cost = order_data["Color Prints"] * 0.50  # Cost per color print
            total_price = binding_cost + ohp_cost + bw_print_cost + color_print_cost

            # Step 3: Display the order details for confirmation
            print("\n📝 Order Details:")
            print(f"Customer Name: {order_data['Customer Name']}")
            print(f"Order Type: {order_data['Order Type']}")
            print(f"Books Count: {order_data['Books Count']}")
            print(f"OHP Sheets: {order_data['OHP Sheets']} (Cost: ${ohp_cost:.2f})")
            print(
                f"Black & White Prints: {order_data['Black & White Prints']} (Cost: ${bw_print_cost:.2f})"
            )
            print(
                f"Color Prints: {order_data['Color Prints']} (Cost: ${color_print_cost:.2f})"
            )
            print(f"Expected Delivery: {order_data['Expected Delivery']}")
            print(f"Order Status: {order_data['Order Status']}")
            print("\n💰 Cost Breakdown:")
            print(f"Binding Cost: ${binding_cost:.2f}")
            print(f"OHP Sheets Cost: ${ohp_cost:.2f}")
            print(f"Black & White Print Cost: ${bw_print_cost:.2f}")
            print(f"Color Print Cost: ${color_print_cost:.2f}")
            print(f"Total Price: ${total_price:.2f}")

            # Step 4: Ask for confirmation
            confirm = (
                input("\nDo you want to place this order? (yes/no/edit): ")
                .strip()
                .lower()
            )
            if confirm in ["yes", "y"]:
                # Step 5: Generate the Order ID and save the order
                order_data["Order ID"] = OrderSaver.generate_order_id()
                order_data["Total Price"] = (
                    total_price  # Add the calculated total price
                )
                OrderSaver.save_order(order_data)
                print(
                    f"✅ Order placed successfully with Order ID: {order_data['Order ID']}"
                )
                break
            elif confirm in ["edit", "e"]:
                print("🔄 Let's edit the order details.")
                continue  # Restart the loop to re-enter order details
            elif confirm in ["no", "n"]:
                print("❌ Order was not placed.")
                break
            else:
                print("❌ Invalid choice. Please enter 'yes', 'no', or 'edit'.")
