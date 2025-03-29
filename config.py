# config.py

# UI Color Theme

COLORS: dict[str, str] = {
    "primary": "#fb8500",  # Main action color
    "secondary": "#ffb703",  # One more color
    "accent": "#3498db",  # Secondary accent for interactive elements
    "text": "#333333",  # Dark gray text for a softer contrast
    "background": "#ffffff",  # Clean white background
    "border": "#ced4da",  # Subtle border color
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
