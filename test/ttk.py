import tkinter as tk
import customtkinter as ctk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Initialize the ttkbootstrap root window
root = ttk.Window(title="Mixed Widgets Example", size=(500, 400))

# Create a customtkinter frame
ctk_frame = ctk.CTkFrame(root, width=200, height=200)
ctk_frame.place(relx=0.5, rely=0.4, anchor="center")

# Create customtkinter widgets (CTkButton and CTkLabel)
ctk_label = ctk.CTkLabel(
    ctk_frame, text="This is CustomTkinter", width=200, height=40, corner_radius=10
)
ctk_label.pack(padx=10, pady=10)

ctk_button = ctk.CTkButton(
    ctk_frame,
    text="Custom Tkinter Button",
    command=lambda: print("CustomTkinter Button clicked"),
)
ctk_button.pack(padx=10, pady=10)

# Create a ttkbootstrap frame
ttk_frame = ttk.Frame(root)
ttk_frame.place(relx=0.5, rely=0.8, anchor="center")

# Create ttkbootstrap widgets (ttk.Label and ttk.Button)
ttk_label = ttk.Label(ttk_frame, text="This is TTKBootstrap", bootstyle=SUCCESS)
ttk_label.pack(padx=10, pady=10)

ttk_button = ttk.Button(
    ttk_frame,
    text="TTKBootstrap Button",
    bootstyle=PRIMARY,
    command=lambda: print("TTKBootstrap Button clicked"),
)
ttk_button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()
