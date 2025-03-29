# filepath: d:\BookBindingOMS\modules\order_saver.py
import sys
import os
from datetime import datetime

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from config import ORDER_FILE, ORDER_FIELDS  # Updated import


class OrderSaver:
    """Handles saving order details to the orders.csv file."""

    @staticmethod
    def generate_order_id() -> str:
        """Generates a unique order ID based on the current date and time."""
        return f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    @staticmethod
    def save_order(order_data: dict) -> str:
        """
        Saves the order details to the orders.csv file and returns the order ID.
        :param order_data: Dictionary containing order details
        :return: Order ID
        """
        with open(ORDER_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=ORDER_FIELDS)
            writer.writerow(order_data)

        print(f"✅ Order {order_data['Order ID']} saved successfully!")
        return order_data["Order ID"]
