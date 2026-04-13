class Order:

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, order_item):
        # Add an item to the order
        self.items.append(order_item)

    def get_total(self):
        # Calculate full order total
        return sum(item.get_total() for item in self.items)