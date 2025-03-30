import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS


class Admin(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, fg_color="transparent")

        # Example Content for Take Order Page
        self.label = ctk.CTkLabel(self, text="Take Order Page", font=("Arial", 18))
        self.label.pack(pady=20)

        self.order_btn = ctk.CTkButton(
            self, text="Admin Pannel", command=self.create_order
        )
        self.order_btn.pack(pady=10)

    def create_order(self) -> None:
        print("Creating a new order...")
