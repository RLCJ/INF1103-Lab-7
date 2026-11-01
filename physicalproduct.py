from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)        # reusing the constructor from the Product class
        self.weight = float(weight)     # Weight in kg

    def display_information(self):
        super().display_information()  # Call the base class method to display common product info
        print(f"Weight: {self.weight} kg")

    def get_fulfilment_info(self):
        """Returns a string with fulfilment information specific to physical products."""
        return f"Product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        # Calculates shipping cost based on weight (base price of 5 +2 dollars per every kg)
        base_fee= 5.0
        rate_per_kg= 2.0
        return base_fee + (self.weight * rate_per_kg)