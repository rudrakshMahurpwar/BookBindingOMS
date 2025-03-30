import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS


class TakeOrder(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, fg_color="transparent")

        # Example Content for Take Order Page
        self.label = ctk.CTkLabel(self, text="Take Order Page", font=("Arial", 18))
        self.label.pack(pady=20)

        self.order_btn = ctk.CTkButton(
            self, text="Create New Order", command=self.create_order
        )
        self.order_btn.pack(pady=10)

    def create_order(self) -> None:
        print("Creating a new order...")


'''
class TakeOrder(ctk.CTkFrame):
    def __init__(self, parent, place_order_callback):
        super().__init__(parent, fg_color=COLORS["background"])
        self.place_order_callback = place_order_callback

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="📦 Take Order",
            font=FONTS["title"],
            text_color=COLORS["primary"],
        )
        self.title_label.pack(pady=10)


        # Customer Name
        self.name_label = ctk.CTkLabel(self, text="Customer Name:")
        self.name_label.pack()
        self.name_entry = ctk.CTkEntry(self, width=250)
        self.name_entry.pack(pady=5)

        # Order Type Dropdown
        self.order_type_label = ctk.CTkLabel(self, text="Order Type:")
        self.order_type_label.pack()
        self.order_type_var = ctk.StringVar(value="Select Order Type")
        self.order_type_menu = ctk.CTkComboBox(
            self,
            values=["PDF Printing", "Page Binding"],
            command=self.toggle_fields,
            variable=self.order_type_var,
        )
        self.order_type_menu.pack(pady=5)

        # Book Count
        self.book_count_label = ctk.CTkLabel(self, text="Number of Books:")
        self.book_count_label.pack()
        self.book_count_entry = ctk.CTkEntry(self, width=100)
        self.book_count_entry.pack(pady=5)

        # Black & White Prints (Only for PDF Printing)
        self.bw_print_label = ctk.CTkLabel(self, text="B/W Prints:")
        self.bw_print_entry = ctk.CTkEntry(self, width=100)

        # Color Prints (Only for PDF Printing)
        self.color_print_label = ctk.CTkLabel(self, text="Color Prints:")
        self.color_print_entry = ctk.CTkEntry(self, width=100)

        # OHP Sheets (For all orders)
        self.ohp_label = ctk.CTkLabel(self, text="OHP Sheets:")
        self.ohp_label.pack()
        self.ohp_entry = ctk.CTkEntry(self, width=100)
        self.ohp_entry.pack(pady=5)

        # Delivery Date
        self.delivery_label = ctk.CTkLabel(
            self, text="Expected Delivery Date (YYYY-MM-DD):"
        )
        self.delivery_label.pack()
        self.delivery_entry = ctk.CTkEntry(self, width=150)
        self.delivery_entry.pack(pady=5)

        # Submit Button
        self.submit_btn = ctk.CTkButton(
            self, text="Place Order", command=self.place_order
        )
        self.submit_btn.pack(pady=20)

        # Status Bar
        self.status_bar = ctk.CTkLabel(self, text="", text_color="red")
        self.status_bar.pack()

    def toggle_fields(self, choice):
        """Enable/Disable fields based on order type."""
        if choice == "PDF Printing":
            self.bw_print_label.pack()
            self.bw_print_entry.pack()
            self.color_print_label.pack()
            self.color_print_entry.pack()
        else:
            self.bw_print_label.pack_forget()
            self.bw_print_entry.pack_forget()
            self.color_print_label.pack_forget()
            self.color_print_entry.pack_forget()

    def place_order(self):
        """Trigger order placement with validation."""
        if not self.name_entry.get().strip():
            self.status_bar.configure(text="⚠ Please enter the customer name!")
            return

        if self.order_type_var.get() == "Select Order Type":
            self.status_bar.configure(text="⚠ Please select an order type!")
            return

        try:
            datetime.strptime(self.delivery_entry.get(), "%Y-%m-%d")
        except ValueError:
            self.status_bar.configure(text="⚠ Invalid date format! Use YYYY-MM-DD")
            return

        self.place_order_callback()
        self.status_bar.configure(
            text="✅ Order placed successfully!", text_color="green"
        )
'''
