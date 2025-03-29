import customtkinter as ctk
import sys
import os

# Add the root directory to sys.path so Python can find config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import config.py
from config import COLORS  # Import the COLORS dictionary from config.py

# Initialize the customtkinter root window
ctk.set_appearance_mode("Light")
root = ctk.CTk()

root.title("Colors Display")

# Set the window size dynamically based on screen size
screen_width: int = root.winfo_screenwidth()
screen_height: int = root.winfo_screenheight()
window_width = int(screen_width * 0.3)
window_height = int(screen_height * 0.52)
root.geometry(f"{window_width}x{window_height}")

# Create a CTkCanvas to hold the color blocks and make it scrollable
canvas = ctk.CTkCanvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Create a CTkScrollbar for vertical scrolling
scrollbar = ctk.CTkScrollbar(root, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the color blocks
color_frame = ctk.CTkFrame(canvas)
canvas.create_window((0, 0), window=color_frame, anchor="center")

# Create a Status Bar in the bottom-left corner with the background color from config.py
status_bar = ctk.CTkLabel(root, text="", anchor="w", height=30)
status_bar.place(relx=0, rely=1.0, anchor="sw", relwidth=1)


# Function to copy color hex code to clipboard and show feedback
def copy_to_clipboard(hex_code, color_block) -> None:
    try:
        root.clipboard_clear()
        root.clipboard_append(hex_code)
        root.update()

        # Update status bar with copied color name and hex code
        status_bar.configure(text=f"Copied: {hex_code}")

        # Change color block to indicate "clicked"
        original_color = color_block.cget("fg_color")
        # color_block.configure(fg_color="lightgray")  # Change to gray temporarily

        # After 300 ms, revert the color block to its original color
        color_block.after(300, lambda: color_block.configure(fg_color=original_color))

    except Exception as e:
        print(f"Error copying to clipboard: {e}")  # Catch any potential errors


# Add each color block and label it beside the block
for idx, (name, color) in enumerate(COLORS.items()):
    color_block = ctk.CTkLabel(
        color_frame,
        text=color,
        width=50,
        height=50,
        fg_color=color,
        corner_radius=10,
        justify="center",
    )
    color_block.grid(row=idx, column=0, padx=10, pady=5)  # Place colors vertically
    color_block.bind(
        "<Button-1>",
        lambda event, color=color, name=name, block=color_block: copy_to_clipboard(
            color, block
        ),
    )  # Bind click to copy color
    color_label = ctk.CTkLabel(
        color_frame, text=f"{name} - {color}", width=200, height=50, anchor="w"
    )
    color_label.grid(
        row=idx, column=1, padx=10, pady=5
    )  # Place the name beside the color block

# Update the scrollable region based on the number of colors
color_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the mainloop
root.mainloop()
