from models.order import Order
from models.order_item import OrderItem


class OrderController:

    # Handles order creation and processing
    def __init__(self, repository, security_config):
        self.repo = repository
        self.security = security_config

    # Creates an order for a user
    def create_order(self, username, product, quantity):

        # Validate quantity given
        if not self.security.strategy.validate_input(str(quantity)):
            self.security.strategy.log_event("Injection attempt in quantity")
            print("Invalid quantity input.")
            return False

        # Validate product names
        if not self.security.strategy.validate_input(product.name):
            self.security.strategy.log_event("Injection attempt in product data")
            print("Suspicious product data detected. Order blocked.")
            return False

        # Check for whether user is valid
        user = self.repo.get_user(username)

        if not user:
            print("User not found.")
            return False

        order = Order(user)

        item = OrderItem(product, quantity)
        order.add_item(item)

        self.repo.add_order(order)

        self.security.strategy.log_event(f"Order created for {username}")

        # When order is completed return total price/value of all items
        print(f"Order placed. Total: £{order.get_total()}")
        return True