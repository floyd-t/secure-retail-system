class OrderItem:
   # Represents a single item within an order
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        # Calculate total price for this item
        return self.product.price * self.quantity