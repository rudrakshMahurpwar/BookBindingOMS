import customtkinter as ctk
from utils.date_picker import DatePicker  # Custom Date Picker Component


class TakeOrder(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure grid layout to ensure full vertical expansion and half-width horizontally
        self.grid_columnconfigure(
            0, weight=1, uniform="half"
        )  # Takes half of the parent frame width
        self.grid_columnconfigure(
            1, weight=1, uniform="half"
        )  # Empty space for balance
        self.grid_rowconfigure(0, weight=1)  # Allow full vertical expansion

        # Add Order Form (Occupies left half of the parent frame)
        self.order_form = OrderForm(self)
        self.order_form.grid(
            row=0, column=0, sticky="nsew", padx=20, pady=10
        )  # Expands fully within its column

        invoice_section = InvoiceSection(self)
        invoice_section.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)


class OrderForm(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(
            parent,
            fg_color="transparent",
            corner_radius=5,
            border_width=1,
            *args,
            **kwargs,
        )

        # Configure Grid for layout management
        self.grid_rowconfigure(1, weight=1)  # Middle frame expands
        self.grid_columnconfigure(0, weight=1)  # Everything stretches horizontally

        # 🔹 Header Section
        self.header = ctk.CTkLabel(
            self,
            text="📋 Order Details",
            font=("Arial", 16, "bold"),
            anchor="w",
            fg_color="black",
            corner_radius=5,
        )
        self.header.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))

        # 🔹 Middle Content Section
        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        self.content_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(10, 10),
        )

        # 🔹 Footer Section (Full-Width)
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        # Customer Name (Always Visible)
        ctk.CTkLabel(self.content_frame, text="Customer Name").pack(
            anchor="w", padx=10, pady=(0, 0)
        )
        self.customer_name_entry = ctk.CTkEntry(
            self.content_frame, placeholder_text="Enter Customer Name"
        )
        self.customer_name_entry.pack(fill="x", padx=10, pady=0)

        # Service Type (Dropdown)
        ctk.CTkLabel(self.content_frame, text="Service Type").pack(
            anchor="w", padx=10, pady=(10, 0)
        )
        self.service_type_dropdown = ctk.CTkComboBox(
            self.content_frame,
            values=["PDF Printing", "Page Binding"],
            command=self.update_fields,  # Update fields on selection change
        )
        self.service_type_dropdown.pack(fill="x", padx=10, pady=0)

        # Expected Due Date (Always Visible)
        self.delivery_date_picker = DatePicker(self.content_frame, "Expected Due Date:")
        self.delivery_date_picker.pack(
            fill="x",
            padx=10,
            pady=5,
            side="bottom",
        )

        # Dynamic Fields Container
        self.dynamic_fields_frame = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color="transparent",
        )
        self.dynamic_fields_frame.pack(
            fill="x",
            padx=10,
            pady=(5, 0),
            expand=True,
        )

        # Reduce Scrollbar Width
        self.dynamic_fields_frame._scrollbar.configure(width=5)

        # Initial field setup
        self.update_fields(self.service_type_dropdown.get())

        # Status Label
        self.status_label = ctk.CTkLabel(
            self.footer, text="Status: Awaiting Order", text_color="gray"
        )
        self.status_label.pack(side="left", padx=10)

        # Footer Buttons
        self.cancel_button = ctk.CTkButton(
            self.footer, text="❌ Cancel", fg_color="red", command=self.cancel_order
        )
        self.cancel_button.pack(side="right", padx=10)

        self.process_order_button = ctk.CTkButton(
            self.footer, text="✅ Prcess Order", command=self.process_order
        )
        self.process_order_button.pack(side="right")

    def process_order(self):
        self.status_label.configure(text="Status: Order Processed", text_color="blue")

    def cancel_order(self):
        self.status_label.configure(text="Status: Order Canceled ❌", text_color="red")

    def update_fields(self, selected_service) -> None:
        """Updates the form fields dynamically based on the selected service type."""
        # Clear previous dynamic fields
        for widget in self.dynamic_fields_frame.winfo_children():
            widget.destroy()

        if selected_service == "PDF Printing":
            self.add_dynamic_field(
                "Number of Black & White Prints", "Enter Number of B&W Prints"
            )
            self.add_dynamic_field(
                "Number of Color Prints", "Enter Number of Color Prints"
            )
            self.add_dynamic_field("Number of OHP Sheets", "Enter Number of OHP Sheets")

        elif selected_service == "Page Binding":
            self.add_dynamic_field("Number of Books", "Enter Number of Books")

    def add_dynamic_field(self, label_text, placeholder):
        """Creates a new input field inside the dynamic section with adjusted spacing."""
        ctk.CTkLabel(self.dynamic_fields_frame, text=label_text).pack(
            anchor="w",
            padx=10,
            pady=(5, 0),
            expand=True,
        )
        ctk.CTkEntry(self.dynamic_fields_frame, placeholder_text=placeholder).pack(
            fill="x", padx=10, pady=(0, 10)
        )


class InvoiceSection(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(
            parent,
            fg_color="transparent",
            corner_radius=5,
            border_width=1,
            *args,
            **kwargs,
        )

        # Configure grid layout
        self.grid_rowconfigure(1, weight=1)  # Middle section expands
        self.grid_columnconfigure(0, weight=1)  # Full width

        # 🔹 Header Section
        self.header_frame = ctk.CTkFrame(self, fg_color="grey")
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        # 🔹 Content Section
        self.content_frame = ctk.CTkFrame(self, fg_color="white")
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.content_frame.grid_rowconfigure(1, weight=1)

        # 🔹 Footer Section
        self.footer_frame = ctk.CTkFrame(self, fg_color="green")
        self.footer_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        # Contents
        ctk.CTkLabel(
            self.header_frame, text="Create Invoice", font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Bill Header (Inside Content Section)
        self.bill_header = ctk.CTkFrame(self.content_frame, fg_color="lightgrey")
        self.bill_header.pack(fill="x", padx=10, pady=(5, 0))
        ctk.CTkLabel(
            self.bill_header, text="Invoice Details", font=("Arial", 14, "bold")
        ).pack(pady=5)

        # Invoice Table Header (Fixed)
        self.table_header = ctk.CTkFrame(self.content_frame, fg_color="gray")
        self.table_header.pack(fill="x", padx=10, pady=5)

        headers = ["Description", "Qty", "Unit Price", "Amount"]
        for i, text in enumerate(headers):
            ctk.CTkLabel(self.table_header, text=text, font=("Arial", 12, "bold")).grid(
                row=0, column=i, padx=10, pady=5
            )

        # Scrollable Table Content
        self.table_frame = ctk.CTkScrollableFrame(self.content_frame)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        ctk.CTkLabel(
            self.footer_frame,
            text="Processing Invoice...",
            font=("Arial", 12, "bold"),
            fg_color="green",
        ).pack(pady=5)
