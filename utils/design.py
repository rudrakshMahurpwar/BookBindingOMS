import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys
import os

# Add the root directory to sys.path so Python can find config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import config.py
from config import COLORS  # Import the COLORS dictionary from config.py

# Initialize the ttkbootstrap root window
root = ttk.Window(title="Colors Display", size=(400, 300))

# Set the window size dynamically based on screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.3)
window_height = int(screen_height * 0.52)
root.geometry(f"{window_width}x{window_height}")

# Create a canvas to hold the color blocks and make it scrollable
canvas = ttk.Frame(root)
canvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side="right", fill="y")

# Create a frame inside the canvas to hold the color blocks
color_frame = ttk.Frame(canvas)
color_frame.pack(fill="both", expand=True)

# Create a Status Bar in the bottom-left corner with the background color from config.py
status_bar = ttk.Label(root, text="", anchor="w", style="primary.TLabel")
status_bar.place(relx=0, rely=1.0, anchor="sw", relwidth=1, height=30)


# Function to copy color hex code to clipboard and show feedback
def copy_to_clipboard(hex_code, color_block) -> None:
    try:
        root.clipboard_clear()
        root.clipboard_append(hex_code)
        root.update()

        # Update status bar with copied color name and hex code
        status_bar.configure(text=f"Copied: {hex_code}")

        # Change color block to indicate "clicked"
        original_color = color_block.cget("background")
        color_block.configure(background="lightgray")  # Temporarily change to gray

        # After 300 ms, revert the color block to its original color
        color_block.after(300, lambda: color_block.configure(background=original_color))

    except Exception as e:
        print(f"Error copying to clipboard: {e}")  # Catch any potential errors


# Add each color block and label it beside the block
for idx, (name, color) in enumerate(COLORS.items()):
    # Creating a label to display color
    color_block = ttk.Label(
        color_frame,
        text=color,
        width=20,
        anchor="center",
        style="success.TLabel",
        background=color,
        foreground=color,
    )  # Set the background to the actual hex color
    color_block.grid(row=idx, column=0, padx=10, pady=5)  # Place colors vertically
    color_block.bind(
        "<Button-1>",
        lambda event, color=color, block=color_block: copy_to_clipboard(color, block),
    )  # Bind click to copy color
    color_label = ttk.Label(color_frame, text=f"{name} - {color}", width=30, anchor="w")
    color_label.grid(
        row=idx, column=1, padx=10, pady=5
    )  # Place the name beside the color block

# Start the main loop
root.mainloop()
