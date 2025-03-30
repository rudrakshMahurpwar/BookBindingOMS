import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import customtkinter as ctk
from modules.order_saver import OrderSaver


class ConfirmationWindow:
    def __init__(
        self, parent, order_data, clear_main_window, update_status_bar
    ) -> None:
        self.parent = parent
        self.order_data = order_data
        self.clear_main_window = clear_main_window
        self.update_status_bar = update_status_bar

    def show(self) -> None:
        confirmation_window = ctk.CTkToplevel(self.parent)
        confirmation_window.title("Order Confirmation")
        confirmation_window.geometry("600x500")

        # Make the confirmation window scrollable
        scrollable_frame = ctk.CTkScrollableFrame(confirmation_window)
        scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Add Title
        ctk.CTkLabel(
            scrollable_frame, text="🧾 Order Invoice", font=("Arial", 18, "bold")
        ).grid(row=0, column=0, columnspan=4, pady=10)

        # Add Customer Details
        ctk.CTkLabel(
            scrollable_frame, text="Customer Details", font=("Arial", 14, "bold")
        ).grid(row=1, column=0, columnspan=4, pady=5, sticky="w")
        customer_details = [
            ("Customer Name", self.order_data["Customer Name"]),
            ("Expected Delivery", self.order_data["Expected Delivery"]),
            ("Order Status", self.order_data["Order Status"]),
        ]
        for i, (key, value) in enumerate(customer_details, start=2):
            ctk.CTkLabel(scrollable_frame, text=f"{key}:", anchor="w").grid(
                row=i, column=0, sticky="w", padx=10, pady=2
            )
            ctk.CTkLabel(scrollable_frame, text=value, anchor="w").grid(
                row=i, column=1, sticky="w", padx=10, pady=2
            )

        # Add Table Headers
        headers = ["Type", "Quantity", "Rate", "Price"]
        header_row = len(customer_details) + 2
        for col, header in enumerate(headers):
            ctk.CTkLabel(
                scrollable_frame, text=header, font=("Arial", 14, "bold"), anchor="w"
            ).grid(row=header_row, column=col, padx=10, pady=5)

        # Add Order Details in Tabular Format
        details = [
            (
                "Books Count",
                self.order_data["Books Count"],
                "$50.00",
                f"${self.order_data['Books Count'] * 50:.2f}",
            ),
            (
                "Black & White Prints",
                self.order_data["Black & White Prints"],
                "$0.10",
                f"${self.order_data['Black & White Prints'] * 0.10:.2f}",
            ),
            (
                "Color Prints",
                self.order_data["Color Prints"],
                "$0.50",
                f"${self.order_data['Color Prints'] * 0.50:.2f}",
            ),
            (
                "OHP Sheets",
                self.order_data["OHP Sheets"],
                "$2.00",
                f"${self.order_data['OHP Sheets'] * 2.00:.2f}",
            ),
        ]

        for row, (item, qty, rate, price) in enumerate(details, start=header_row + 1):
            ctk.CTkLabel(scrollable_frame, text=item, anchor="w").grid(
                row=row, column=0, sticky="w", padx=10, pady=5
            )
            ctk.CTkLabel(scrollable_frame, text=qty, anchor="w").grid(
                row=row, column=1, sticky="w", padx=10, pady=5
            )
            ctk.CTkLabel(scrollable_frame, text=rate, anchor="w").grid(
                row=row, column=2, sticky="w", padx=10, pady=5
            )
            ctk.CTkLabel(scrollable_frame, text=price, anchor="w").grid(
                row=row, column=3, sticky="w", padx=10, pady=5
            )

        # Add Total Price
        total_row = header_row + len(details) + 1
        ctk.CTkLabel(
            scrollable_frame, text="Total Price", font=("Arial", 14, "bold"), anchor="w"
        ).grid(row=total_row, column=2, sticky="w", padx=10, pady=10)
        ctk.CTkLabel(
            scrollable_frame,
            text=f"${self.order_data['Total Price']:.2f}",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).grid(row=total_row, column=3, sticky="w", padx=10, pady=10)

        # Add Buttons for Actions
        button_frame = ctk.CTkFrame(confirmation_window)
        button_frame.pack(fill="x", side="bottom", pady=10)

        def place_order() -> None:
            self.order_data["Order ID"] = OrderSaver.generate_order_id()
            OrderSaver.save_order(self.order_data)
            self.update_status_bar("✅ Order placed successfully!", "green")
            confirmation_window.destroy()
            self.clear_main_window()

        def modify_order() -> None:
            self.update_status_bar("❌ Update the Order.", "blue")
            confirmation_window.destroy()

        def cancel_order() -> None:
            self.update_status_bar("❌ Order not placed.", "red")
            confirmation_window.destroy()
            self.clear_main_window()

        # Add Buttons with Equal Spacing
        place_button = ctk.CTkButton(
            button_frame, text="Place Order", command=place_order, fg_color="green"
        )
        modify_button = ctk.CTkButton(
            button_frame, text="Modify Order", command=modify_order, fg_color="blue"
        )
        cancel_button = ctk.CTkButton(
            button_frame, text="Cancel Order", command=cancel_order, fg_color="red"
        )

        place_button.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        modify_button.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        cancel_button.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

        # Configure equal column weights for buttons
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)
