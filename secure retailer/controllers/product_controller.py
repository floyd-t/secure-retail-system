from models.product import Product


class ProductController:

    # Simulates catalogue of items
    def __init__(self, security_config):
        self.security = security_config

        # Simple in-memory product store
        self.products = {}

    # Adds product to the system
    def add_product(self, product_id, name, price):

        # Input validation aims to prevent injection attacks
        if not self.security.strategy.validate_input(name):
            self.security.strategy.log_event("Injection attempt in product name")
            print("Invalid product name.")
            return False

        # Details for each product
        product = Product(product_id, name, price)
        self.products[product_id] = product

        return True

    def list_products(self):
        # For displaying all products
        for p in self.products.values():
            print(f"{p.product_id}: {p.name} - £{p.price}")

    def get_product(self, product_id):
        return self.products.get(product_id)