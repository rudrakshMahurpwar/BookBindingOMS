from datetime import date

import customtkinter as ctk
from tkcalendar import DateEntry


class NewOrderUI:
    def __init__(self, parent, place_order_callback, toggle_fields_callback) -> None:
        self.parent = parent
        self.place_order_callback = place_order_callback
        self.toggle_fields_callback = toggle_fields_callback

    def create_ui(self, tab) -> None:
        """Create the New Order UI on the given tab."""
        label = ctk.CTkLabel(
            tab, text="📌 Create New Order", font=("Arial", 20, "bold")
        )
        label.pack(pady=10)

        # Customer Name
        self.customer_entry = ctk.CTkEntry(tab, placeholder_text="Enter Customer Name")
        self.customer_entry.pack(pady=5)

        # Order Type
        self.order_type = ctk.StringVar(value="Select Order Type")
        self.order_dropdown = ctk.CTkComboBox(
            tab,
            variable=self.order_type,
            values=["PDF Printing", "Page Binding"],
            command=self.toggle_fields_callback,
        )
        self.order_dropdown.pack(pady=5)

        # Number of Books (Initially Hidden)
        self.book_count_entry = ctk.CTkEntry(tab, placeholder_text="Number of Books")
        self.book_count_entry.pack_forget()

        # Black & White Prints (Initially Hidden)
        self.bw_print_entry = ctk.CTkEntry(tab, placeholder_text="Black & White Prints")
        self.bw_print_entry.pack_forget()

        # Color Prints (Initially Hidden)
        self.color_print_entry = ctk.CTkEntry(tab, placeholder_text="Color Prints")
        self.color_print_entry.pack_forget()

        # OHP Sheets (Initially Hidden)
        self.ohp_count_entry = ctk.CTkEntry(tab, placeholder_text="OHP Sheets")
        self.ohp_count_entry.pack_forget()

        # Expected Delivery Date (Date Picker)
        date_label = ctk.CTkLabel(tab, text="Expected Delivery Date:")
        date_label.pack(pady=5)
        self.delivery_date_picker = DateEntry(
            tab, date_pattern="yyyy-mm-dd"
        )  # Date picker widget
        self.delivery_date_picker.pack(pady=5)

        # Frame for Place Order Button (to keep it at the bottom)
        button_frame = ctk.CTkFrame(tab)
        button_frame.pack(fill="x", side="bottom", pady=10)

        # Place Order Button
        place_order = ctk.CTkButton(
            button_frame, text="Place Order", command=self.place_order_callback
        )
        place_order.pack(pady=10)

    def get_inputs(self) -> dict:
        """Retrieve the inputs from the New Order form."""
        return {
            "customer_name": self.customer_entry.get(),
            "order_type": self.order_type.get(),
            "book_count": self.book_count_entry.get(),
            "bw_prints": self.bw_print_entry.get(),
            "color_prints": self.color_print_entry.get(),
            "ohp_count": self.ohp_count_entry.get(),
            "delivery_date": self.delivery_date_picker.get(),
        }

    def clear_inputs(self) -> None:
        """Clear all input fields in the New Order form."""
        self.customer_entry.delete(0, "end")
        self.order_type.set("Select Order Type")
        self.book_count_entry.delete(0, "end")
        self.bw_print_entry.delete(0, "end")
        self.color_print_entry.delete(0, "end")
        self.ohp_count_entry.delete(0, "end")
        self.delivery_date_picker.set_date(date.today())
