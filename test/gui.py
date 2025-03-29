import customtkinter as ctk
from tkcalendar import DateEntry  # Import DateEntry for the date picker
from modules.order_manager import OrderManager
from modules.order_saver import OrderSaver
from modules.order_input import OrderInput
from datetime import datetime
from config import COLORS
from windows.confirmation_window import ConfirmationWindow

# Initialize CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class BookBindingApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Book Binding Order Management System...")

        # App Configuration
        self.title("📚 Book Binding Order Management")
        self.geometry("800x600")
        self.configure(bg=COLORS["background"])

        # Create Tabs
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=20)

        # Tabs
        self.new_order_tab: ctk.CTkFrame = self.tabview.add("🆕 New Order")
        self.manage_orders_tab: ctk.CTkFrame = self.tabview.add("📋 Manage Orders")

        # Status Bar
        self.status_bar = ctk.CTkLabel(
            self, text="", fg_color="lightgray", anchor="w", font=("Arial", 12)
        )
        self.status_bar.pack(fill="x", side="bottom")

        # Load UI
        self.new_order_ui()
        self.manage_orders_ui()

    # 📌 UI for New Order
    def new_order_ui(self) -> None:
        label = ctk.CTkLabel(
            self.new_order_tab, text="📌 Create New Order", font=("Arial", 20, "bold")
        )
        label.pack(pady=10)

        # Customer Name
        self.customer_entry = ctk.CTkEntry(
            self.new_order_tab, placeholder_text="Enter Customer Name"
        )
        self.customer_entry.pack(pady=5)

        # Order Type
        self.order_type = ctk.StringVar(value="Select Order Type")
        self.order_dropdown = ctk.CTkComboBox(
            self.new_order_tab,
            variable=self.order_type,
            values=["PDF Printing", "Page Binding"],
            command=self.toggle_fields,
        )
        self.order_dropdown.pack(pady=5)

        # Number of Books (Initially Hidden)
        self.book_count_entry = ctk.CTkEntry(
            self.new_order_tab, placeholder_text="Number of Books"
        )
        self.book_count_entry.pack_forget()

        # Black & White Prints (Initially Hidden)
        self.bw_print_entry = ctk.CTkEntry(
            self.new_order_tab, placeholder_text="Black & White Prints"
        )
        self.bw_print_entry.pack_forget()

        # Color Prints (Initially Hidden)
        self.color_print_entry = ctk.CTkEntry(
            self.new_order_tab, placeholder_text="Color Prints"
        )
        self.color_print_entry.pack_forget()

        # OHP Sheets (Initially Hidden)
        self.ohp_count_entry = ctk.CTkEntry(
            self.new_order_tab, placeholder_text="OHP Sheets"
        )
        self.ohp_count_entry.pack_forget()

        # Expected Delivery Date (Date Picker)
        date_label = ctk.CTkLabel(self.new_order_tab, text="Expected Delivery Date:")
        date_label.pack(pady=5)
        self.delivery_date_picker = DateEntry(
            self.new_order_tab, date_pattern="yyyy-mm-dd"
        )  # Date picker widget
        self.delivery_date_picker.pack(pady=5)

        # Frame for Place Order Button (to keep it at the bottom)
        button_frame = ctk.CTkFrame(self.new_order_tab)
        button_frame.pack(fill="x", side="bottom", pady=10)

        # Place Order Button
        place_order = ctk.CTkButton(
            button_frame, text="Place Order", command=self.place_order
        )
        place_order.pack(pady=10)

    # 🔹 Function to Toggle Fields Based on Order Type
    def toggle_fields(self, choice: str) -> None:
        """Enable/Disable fields based on order type and dynamically show relevant fields."""
        if choice == "PDF Printing":
            # Show fields relevant to PDF Printing
            self.book_count_entry.pack(pady=5)
            self.bw_print_entry.pack(pady=5)
            self.color_print_entry.pack(pady=5)
            self.ohp_count_entry.pack(pady=5)
        elif choice == "Page Binding":
            # Show only fields relevant to Page Binding
            self.book_count_entry.pack(pady=5)
            self.bw_print_entry.pack_forget()
            self.color_print_entry.pack_forget()
            self.ohp_count_entry.pack(pady=5)
        else:
            # Hide all fields if no valid order type is selected
            self.book_count_entry.pack_forget()
            self.bw_print_entry.pack_forget()
            self.color_print_entry.pack_forget()
            self.ohp_count_entry.pack_forget()

    # 🔹 Function to Handle Order Submission
    def place_order(self) -> None:
        customer_name = self.customer_entry.get()
        order_type = self.order_type.get()
        book_count = self.book_count_entry.get()
        bw_prints = self.bw_print_entry.get() if order_type == "PDF Printing" else 0
        color_prints = (
            self.color_print_entry.get() if order_type == "PDF Printing" else 0
        )
        ohp_count = self.ohp_count_entry.get()
        delivery_date = (
            self.delivery_date_picker.get()
        )  # Get the selected date from the date picker

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
            if not self.validate_input(bw_prints, "Black & White Prints"):
                return
            if not self.validate_input(color_prints, "Color Prints"):
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

        # Calculate Total Price using OrderInput
        total_price: float = OrderInput.calculate_total_price(
            int(book_count), int(bw_prints), int(color_prints), int(ohp_count)
        )

        # Prepare Order Data
        order_data: dict = {
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

    def validate_input(
        self, value: str, field_name: str, is_required: bool = True, data_type=int
    ) -> bool:
        """
        Validates an input field for emptiness and data type.

        Args:
            value (str): The input value to validate.
            field_name (str): The name of the field (used for error messages).
            is_required (bool): Whether the field is required (default: True).
            data_type (type): The expected data type (default: int).

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        try:
            if is_required and not value.strip():  # Check if the field is empty
                raise ValueError("Field is empty")
            if data_type == int:
                value = int(value)  # type: ignore # Convert to integer if required
            elif data_type == float:
                value = float(value)  # type: ignore # Convert to float if required
            return True
        except ValueError as e:
            if str(e) == "Field is empty":
                self.update_status_bar(f"⚠ Please fill in the {field_name}!", "red")
            else:
                self.update_status_bar(
                    f"⚠ {field_name} must be a valid {data_type.__name__}!", "red"
                )
            return False

    def update_status_bar(self, message: str, text_color: str = "black") -> None:
        """Update the status bar with a message and text color."""
        self.status_bar.configure(text=message, text_color=text_color)

    def clear_main_window(self) -> None:
        """Clear all input fields in the main window."""
        self.customer_entry.delete(0, "end")
        self.order_type.set("Select Order Type")
        self.book_count_entry.delete(0, "end")
        self.bw_print_entry.delete(0, "end")
        self.color_print_entry.delete(0, "end")
        self.ohp_count_entry.delete(0, "end")
        self.delivery_date_picker.set_date(datetime.now())

    # 📌 UI for Managing Orders
    def manage_orders_ui(self) -> None:
        label = ctk.CTkLabel(
            self.manage_orders_tab,
            text="📋 Manage Orders (Coming Soon)",
            font=("Arial", 20, "bold"),
        )
        label.pack(pady=10)

    def show_confirmation_window(self, order_data: dict) -> None:
        confirmation_window = ConfirmationWindow(
            self, order_data, self.clear_main_window, self.update_status_bar
        )
        confirmation_window.show()


# Run the App
if __name__ == "__main__":
    app = BookBindingApp()
    app.mainloop()
