import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS
from windows.confirmation_window import ConfirmationWindow
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from windows.new_order_ui import NewOrderUI  # Import the New Order UI

# Set the theme to light mode
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("theme.json")


class BookBindingApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Book Binding Order Management System...")

        # Fetch screen width & height
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()

        # Calculate window size
        window_width: int = int(screen_width * 0.28)
        window_height: int = int(screen_height * 0.9)

        # App Configuration
        self.title("📚 Book Binding Order Management")
        self.geometry(f"{window_width}x{window_height}+950+10")

        # Create Tabs
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=10)

        # Tabs
        self.new_order_tab: ctk.CTkFrame = self.tabview.add("🆕 New Order")
        self.manage_orders_tab: ctk.CTkFrame = self.tabview.add("📋 Manage Orders")

        # Universal Tab Style (Applies to all tabs)
        self.tabview.configure(border_width=0)

        # Status Bar
        self.status_bar = ctk.CTkLabel(self, text="", anchor="nw", padx=20)
        self.status_bar.pack(fill="x", side="bottom")

        # Initialize New Order UI
        self.new_order_ui = NewOrderUI(self, self.place_order, self.toggle_fields)
        self.new_order_ui.create_ui(self.new_order_tab)

        # Load Manage Orders UI
        self.manage_orders_ui()

    # 🔹 Function to Toggle Fields Based on Order Type
    def toggle_fields(self, choice: str) -> None:
        """Enable/Disable fields based on order type and dynamically show relevant fields."""
        if choice == "PDF Printing":
            # Show fields relevant to PDF Printing
            self.new_order_ui.book_count_entry.pack(pady=10)
            self.new_order_ui.bw_print_entry.pack(pady=10)
            self.new_order_ui.color_print_entry.pack(pady=10)
            self.new_order_ui.ohp_count_entry.pack(pady=10)

        elif choice == "Page Binding":
            # Show only fields relevant to Page Binding
            self.new_order_ui.book_count_entry.pack(pady=10)
            self.new_order_ui.bw_print_entry.pack_forget()
            self.new_order_ui.color_print_entry.pack_forget()
            self.new_order_ui.ohp_count_entry.pack(pady=10)

        else:
            # Hide all fields if no valid order type is selected
            self.new_order_ui.book_count_entry.pack_forget()
            self.new_order_ui.bw_print_entry.pack_forget()
            self.new_order_ui.color_print_entry.pack_forget()
            self.new_order_ui.ohp_count_entry.pack_forget()

    # 🔹 Function to Handle Order Submission
    def place_order(self) -> None:
        inputs = self.new_order_ui.get_inputs()
        customer_name = inputs["customer_name"]
        order_type = inputs["order_type"]
        book_count = inputs["book_count"]
        bw_prints = inputs["bw_prints"] if order_type == "PDF Printing" else 0
        color_prints = inputs["color_prints"] if order_type == "PDF Printing" else 0
        ohp_count = inputs["ohp_count"]
        delivery_date = inputs["delivery_date"]

        # Validate Data
        if not customer_name.strip():
            self.update_status_bar("⚠ Please fill in the customer name!", "red")
            return

        if order_type == "Select Order Type":
            self.update_status_bar("⚠ Please select a valid order type!", "red")
            return

        if not self.validate_input(book_count, "Number of Books"):
            return

        if order_type == "PDF Printing":
            if not self.validate_input(bw_prints, "Black & White Prints"):  # type: ignore
                return
            if not self.validate_input(color_prints, "Color Prints"):  # type: ignore
                return

        if not self.validate_input(ohp_count, "OHP Sheets"):
            return

        try:
            datetime.strptime(delivery_date, "%Y-%m-%d")  # Validate Date
        except ValueError:
            self.update_status_bar(
                "⚠ Expected Delivery Date must be in YYYY-MM-DD format!", "red"
            )
            return

        # Calculate Total Price
        total_price: float = (
            int(book_count) * 50
            + int(bw_prints) * 0.10
            + int(color_prints) * 0.50
            + int(ohp_count) * 2.00
        )

        # Prepare Order Data
        order_data = {
            "Customer Name": customer_name,
            "Order Type": order_type,
            "Books Count": int(book_count),
            "Black & White Prints": int(bw_prints),
            "Color Prints": int(color_prints),
            "OHP Sheets": int(ohp_count),
            "Expected Delivery": delivery_date,
            "Order Status": "Pending",
            "Total Price": total_price,
        }

        # Show Confirmation Window
        self.show_confirmation_window(order_data)

    def update_status_bar(self, message: str, text_color: str = "black") -> None:
        """Update the status bar with a message and text color."""
        self.status_bar.configure(text=message, text_color=text_color)

    def manage_orders_ui(self) -> None:
        label = ctk.CTkLabel(
            self.manage_orders_tab,
            text="📋 Manage Orders (Coming Soon)",
            font=("Arial", 50, "bold"),
        )
        label.pack(pady=10)

    def show_confirmation_window(self, order_data: dict) -> None:
        self.withdraw

        confirmation_window = ConfirmationWindow(
            self, order_data, self.new_order_ui.clear_inputs, self.update_status_bar
        )
        confirmation_window.show()

    def validate_input(self, value: str, field_name: str) -> bool:
        """Validate the input value for a specific field."""
        if not value.strip():  # Check if the value is empty
            self.update_status_bar(f"⚠ {field_name} cannot be empty!", "red")
            return False
        if not value.isdigit():  # Check if the value is numeric
            self.update_status_bar(f"⚠ {field_name} must be a number!", "red")
            return False
        return True


# Run the App
if __name__ == "__main__":
    app = BookBindingApp()
    app.mainloop()
