import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS


class Footer(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, fg_color=COLORS["text"], corner_radius=10)
        # self.configure(height=20)

        # Example Footer Content
        self.footer_label = ctk.CTkLabel(
            self,
            text="© 2025 Shree Balaji Pringting Press. All rights Rresered",
            font=("Arial", 10, "bold"),
            text_color="white",
        )
        self.footer_label.pack(pady=10)
