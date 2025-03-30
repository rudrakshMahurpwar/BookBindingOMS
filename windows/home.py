import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS


class Home(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent, fg_color="transparent")

        # Example Content for Take Order Page
        self.label = ctk.CTkLabel(
            self,
            text="This is a Home Page",
        )
        self.label.pack(pady=20)
