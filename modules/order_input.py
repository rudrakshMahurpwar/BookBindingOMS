import datetime


class OrderInput:
    """Handles taking order details from the user."""

    @staticmethod
    def take_order() -> dict:
        """
        Takes order details from the user and returns a structured dictionary.
        """
        print("\n📝 Enter Order Details:")

        customer_name: str = input("Customer Name: ").strip()

        # Order Type Selection
        print("\nOrder Type:")
        print("1️⃣ PDF File for Printing & Binding")
        print("2️⃣ Pre-Printed Pages for Binding")
        order_type: str = input("Select Order Type (1/2): ").strip()

        if order_type == "1":
            order_type = "PDF Printing & Binding"
        elif order_type == "2":
            order_type = "Pre-Printed Pages Binding"
        else:
            print("❌ Invalid selection. Defaulting to 'PDF Printing & Binding'.")
            order_type = "PDF Printing & Binding"

        # Number of Books
        while True:
            try:
                books_count: int = int(input("Number of Books: "))
                if books_count > 0:
                    break
                print("❌ Books count must be at least 1.")
            except ValueError:
                print("❌ Please enter a valid number.")

        # If order includes printing, ask for print details
        if order_type == "PDF Printing & Binding":
            black_white_prints: int = int(input("Black & White Prints: ") or 0)
            color_prints: int = int(input("Color Prints: ") or 0)
        else:
            black_white_prints = 0
            color_prints = 0

        # OHP Sheets (Used for both types)
        ohp_sheets: int = int(input("OHP Sheets (if any): ") or 0)

        # Expected Delivery Date
        while True:
            expected_delivery: str = input(
                "Expected Delivery Date (YYYY-MM-DD): "
            ).strip()
            try:
                expected_delivery_date: datetime.date = datetime.datetime.strptime(
                    expected_delivery, "%Y-%m-%d"
                ).date()
                if expected_delivery_date >= datetime.date.today():
                    break
                print("❌ Delivery date cannot be in the past.")
            except ValueError:
                print("❌ Please enter a valid date in YYYY-MM-DD format.")

        # Default Order Status
        order_status = "Pending"

        # Calculate Total Price
        total_price: float = OrderInput.calculate_total_price(
            books_count, black_white_prints, color_prints, ohp_sheets
        )

        # Structure the order data as a dictionary
        order_data: dict = {
            "Customer Name": customer_name,
            "Order Type": order_type,
            "Books Count": books_count,
            "Black & White Prints": black_white_prints,
            "Color Prints": color_prints,
            "OHP Sheets": ohp_sheets,
            "Expected Delivery": expected_delivery,
            "Order Status": order_status,
            "Total Price": total_price,
        }

        return order_data

    @staticmethod
    def calculate_total_price(
        books_count: int,
        black_white_prints: int = 0,
        color_prints: int = 0,
        ohp_sheets: int = 0,
    ) -> float:
        """
        Calculates the total price of the order based on the provided details.

        Args:
            books_count (int): Number of books in the order.
            black_white_prints (int): Number of black & white prints.
            color_prints (int): Number of color prints.
            ohp_sheets (int): Number of OHP sheets.

        Returns:
            float: Total price of the order.
        """
        # Define pricing
        price_per_book_binding = 50.0  # Cost for binding one book
        price_per_bw_print = 0.10  # Cost per black & white print
        price_per_color_print = 0.50  # Cost per color print
        price_per_ohp_sheet = 2.00  # Cost per OHP sheet

        # Calculate individual costs
        binding_cost: float = books_count * price_per_book_binding
        bw_print_cost: float = black_white_prints * price_per_bw_print
        color_print_cost: float = color_prints * price_per_color_print
        ohp_sheet_cost: float = ohp_sheets * price_per_ohp_sheet

        # Calculate total price
        total_price: float = (
            binding_cost + bw_print_cost + color_print_cost + ohp_sheet_cost
        )

        return total_price
