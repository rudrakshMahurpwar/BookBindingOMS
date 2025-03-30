import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry

import sys
import os

# Add the root directory to sys.path so Python can find config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.date_picker import DatePicker
from config import COLORS, FONTS


class TakeOrder(ctk.CTkFrame):
    def __init__(self, parent, fg_color=COLORS["primary"]) -> None:
        super().__init__(parent)

        # ----------- CREATING FRAMES ------------#
        # Left Frame

        self.left_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            corner_radius=5,
            border_width=1,
            label_text="Invoice Details",
            label_anchor="w",
            orientation="vertical",
            scrollbar_button_color="lightgrey",
            scrollbar_button_hover_color="grey",
        )

        # Right Frame
        self.right_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            corner_radius=5,
            border_width=1,
            label_text="Invoice Table",
            label_anchor="w",
            orientation="vertical",
            scrollbar_button_color="lightgrey",
            scrollbar_button_hover_color="grey",
        )

        # Positioning Frames
        self.left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=(10, 5),
        )

        self.right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=(5, 10),
        )

        # Customer Name
        customer_name_lable = ctk.CTkLabel(
            self.left_frame,
            text="Customer Name",
        )
        customer_name_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )

        customer_name_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter Customer Name",
        )
        customer_name_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Sevice Type
        service_type_lable = ctk.CTkLabel(
            self.left_frame,
            text="Sevice Type",
        )
        service_type_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )
        service_type_entry = ctk.CTkComboBox(
            self.left_frame,
            values=["PDF Printing", "Page Binding"],
        )
        service_type_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Number of Books
        number_of_books_lable = ctk.CTkLabel(
            self.left_frame,
            text="Number of Books",
        )
        number_of_books_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )

        number_of_books_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter Number of Books",
        )
        number_of_books_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Black & White Prints
        b_w_prints_lable = ctk.CTkLabel(
            self.left_frame,
            text="Number of Black & White Prints",
        )
        b_w_prints_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )

        b_w_prints_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter Number of Black & White Prints",
        )
        b_w_prints_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Color Prints
        color_prints_lable = ctk.CTkLabel(
            self.left_frame,
            text="Number of Color Prints",
        )
        color_prints_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )

        color_prints_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter Number of Color Prints",
        )
        color_prints_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Number of OHP Sheets
        ohp_sheets_lable = ctk.CTkLabel(
            self.left_frame,
            text="Number of OPH Sheets",
        )
        ohp_sheets_lable.pack(
            anchor="w",
            padx=20,
            pady=(10, 0),
        )

        ohp_sheets_entry = ctk.CTkEntry(
            self.left_frame,
            placeholder_text="Enter Number of OHP Sheets",
        )
        ohp_sheets_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        # Inside `TakeOrder` class, replace old date entry:
        self.delivery_date_picker = DatePicker(
            self.left_frame,
            "Expected Delivery Date:",
        )
        self.delivery_date_picker.pack(
            fill="x",
            padx=20,
            pady=10,
        )

        # Frame for Place Order Button (to keep it at the bottom)
        button_frame = ctk.CTkFrame(
            self.left_frame,
        )
        button_frame.pack(
            fill="x",
            side="bottom",
            padx=20,
            pady=(10, 0),
        )

        # Place Order Button
        place_order = ctk.CTkButton(
            button_frame,
            text="Place Order",
        )
        place_order.pack(
            padx=20,
            pady=(10, 0),
        )
