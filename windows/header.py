import customtkinter as ctk
from datetime import datetime
from config import COLORS, FONTS

from windows.home import Home
from windows.take_order import TakeOrder
from windows.manage_order import ManageOrder
from windows.admin import Admin


class Header(ctk.CTkFrame):
    def __init__(self, parent, content_frame) -> None:
        super().__init__(
            parent, fg_color=COLORS["primary"], height=60, corner_radius=50
        )
        self.content_frame = content_frame

        # Prevent shrinking
        self.pack_propagate(False)
        self.grid_columnconfigure(
            (0, 1, 2), weight=1
        )  # Three sections: Left, Center, Right
        self.grid_rowconfigure(0, weight=1)

        # ========== LEFT: LOGO ==========
        self.logo_label = ctk.CTkLabel(
            self, text="📖", font=("Arial", 22, "bold"), text_color="white"
        )
        self.logo_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        # ========== CENTER: EMPTY SPACE (Keeps Buttons on the Right) ==========
        self.grid_columnconfigure(1, weight=1)  # Ensures space between logo & buttons

        # ========== RIGHT: NAVIGATION BUTTONS & ADMIN ICON ==========
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.grid(row=0, column=2, sticky="e", padx=20, pady=10)

        # NAVIGATION BUTTONS
        self.home_btn = ctk.CTkButton(
            self.right_frame,
            text="Home",
            width=100,
            command=self.show_home,
        )
        self.home_btn.pack(side="left", padx=10)

        self.take_orders_btn = ctk.CTkButton(
            self.right_frame,
            text="Take Order",
            width=100,
            command=self.show_take_order,
        )
        self.take_orders_btn.pack(side="left", padx=10)

        self.manage_orders_btn = ctk.CTkButton(
            self.right_frame,
            text="Manage Orders",
            width=100,
            command=self.show_manage_orders,
        )
        self.manage_orders_btn.pack(side="left", padx=10)

        # ADMIN BUTTON
        self.admin_btn = ctk.CTkButton(
            self.right_frame,
            text="👤 Admin",
            font=("Arial", 16, "bold"),
            fg_color="transparent",  # Initially transparent
            text_color="white",
            hover_color=COLORS["secondary"],  # Changes on hover
            width=100,
            command=self.show_admin,
        )
        self.admin_btn.pack(side="left", padx=(10, 0))  # Space between buttons & admin

    def show_home(self) -> None:
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        home_page = Home(self.content_frame)
        home_page.pack(fill="both", expand=True)

    def show_take_order(self):
        print("Navigating to Take Order Page...")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        take_order_page = TakeOrder(self.content_frame)
        take_order_page.pack(fill="both", expand=True)

    def show_manage_orders(self) -> None:
        print("Navigating to Manage Orders Page...")
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        manage_order_page = ManageOrder(self.content_frame)
        manage_order_page.pack(fill="both", expand=True)

    def show_admin(self) -> None:
        print("Navigating to Admin Page...")
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        admin_page = Admin(self.content_frame)
        admin_page.pack(fill="both", expand=True)
