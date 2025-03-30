# config.py

# UI Color Theme

COLORS: dict[str, str] = {
    "primary": "#fb8500",  # Main action color
    "secondary": "#ffb703",  # One more color
    "accent": "#f7e17e",  # Secondary accent for interactive elements
    "text": "#333333",  # Dark gray text for a softer contrast
    "background": "#f5f3f4",  # Clean white background
    "border": "#ced4da",  # Subtle border color
    "selected": "#fb8500",  # Selected state color
    "selectedhover": "#fb8005",  # Hover color for selected items
    "unselected": "#ffb703",  # Selected state color
    "unselectedhover": "#ffb000",  # Hover color for selected items
    "button": "#fb8500",  # Button color
    "button_hover": "#ffb703",  # Button hover color
    "button_active": "#ffb703",  # Button active color
    "button_disabled": "#6c757d",  # Button disabled color
    "disabled": "#6c757d",  # Disabled state color
    "active": "#ffb703",  # Active state color
    "highlight": "#ffb703",  # Highlight color
    "success": "#28a745",  # Success color
    "error": "#dc3545",  # Error color
    "warning": "#ffc107",  # Warning color
    "info": "#17a2b8",  # Info color
    "light": "#f8f9fa",  # Light color
    "dark": "#343a40",  # Dark color
    "link": "#007bff",  # Link color
    "link_hover": "#0056b3",  # Link hover color
    "link_active": "#004085",  # Link active color
    "link_visited": "#6f42c1",  # Link visited color
    "link_visited_hover": "#5a6268",  # Link visited hover color
    "link_visited_active": "#343a40",  # Link visited active color
    "link_visited_disabled": "#6c757d",  # Link visited disabled color
    "link_visited_disabled_hover": "#adb5bd",  # Link visited disabled hover color
    "link_visited_disabled_active": "#495057",  # Link visited disabled active color
    "link_visited_disabled_active_hover": "#343a40",  # Link visited disabled active hover color
    "link_visited_disabled_active_hover_disabled": "#6c757d",  # Link visited disabled active hover disabled color
}

FONTS: dict[str, tuple[str, int, str]] = {
    "heading": ("Arial", 18, "bold"),
    "text": ("Arial", 14, "normal"),
}

# File Paths
ORDER_CSV = "data/orders.csv"
PRICING_CSV = "data/pricing.csv"

# Define the path for storing order data
ORDER_FILE = ORDER_CSV

# Define the order fields
ORDER_FIELDS: list[str] = [
    "Order ID",
    "Customer Name",
    "Order Type",
    "Books Count",
    "Black & White Prints",
    "Color Prints",
    "OHP Sheets",
    "Expected Delivery",
    "Order Status",
    "Total Price",
]
