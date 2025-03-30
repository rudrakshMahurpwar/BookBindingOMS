import customtkinter as ctk
from config import COLORS  # Importing color theme

from windows.header import Header
from windows.footer import Footer
from windows.take_order import TakeOrder


# Set the theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("theme.json")


class BookBindingApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Book Binding Order Management System...")

        # Fetch screen width & height
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()

        # Calculate window size
        window_width: int = int(screen_width * 0.8)
        window_height: int = int(screen_height * 0.9)

        # App Configuration
        self.title("📚 Book Binding Order Management")
        self.geometry(f"{window_width}x{window_height}+10+10")

        # ---------------- LAYOUT CONFIGURATION ---------------- #
        self.grid_rowconfigure(1, weight=1)  # Middle section expands
        self.grid_columnconfigure(0, weight=1)  # Expand to fill width

        # ---------------- CREATING FRAMES ---------------- #
        self.header_frame = ctk.CTkFrame(
            self,
            height=50,
            fg_color="transparent",
            corner_radius=50,
        )
        self.content = ctk.CTkFrame(
            self,
            fg_color=COLORS["accent"],
            corner_radius=15,
        )
        self.footer_frame = ctk.CTkFrame(
            self,
            height=35,
            fg_color="transparent",
        )

        # ---------------- HEADER ---------------- #
        self.header_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(10, 0))

        # Prevent Expansion
        self.header_frame.grid_propagate(False)
        self.header_frame.pack_propagate(False)
        self.grid_rowconfigure(0, weight=0)  # Stops row from stretching

        # Inject Header content from `windows.header.Header`
        self.header = Header(self.header_frame, self.content)  # Pass content frame
        self.header.pack(fill="both", expand=True)

        # ---------------- CONTENT (Middle Section) ---------------- #
        self.content.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.content.grid_columnconfigure((0, 1), weight=1)
        self.content.grid_rowconfigure(0, weight=1)

        # Inject TakeOrder frame by default
        self.landing_page: None = TakeOrder(self.content).pack(fill="both", expand=True)

        # ---------------- FOOTER ---------------- #
        self.footer_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 10))

        # Prevent Expansion
        self.footer_frame.grid_propagate(False)
        self.footer_frame.pack_propagate(False)
        self.grid_rowconfigure(2, weight=0)  # Stops row from stretching

        # Inject Footer content from `windows.header.Header`
        self.footer = Footer(self.footer_frame)
        self.footer.pack(fill="both", expand=True)  # Ensures it fills the footer frame


if __name__ == "__main__":
    app = BookBindingApp()
    app.mainloop()
    print("Exiting Book Binding Order Management System...")
