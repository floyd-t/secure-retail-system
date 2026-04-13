from data.repository import DataRepository
from security.security_config import SecurityConfig
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController
from controllers.auth_controller import AuthController
from attacks.injection import injection_attack


def test_system():
    # Secure mode
    print("=== SECURE MODE ===")

    repo = DataRepository()
    security = SecurityConfig(True)

    auth = AuthController(repo, security)
    product_ctrl = ProductController(security)
    order_ctrl = OrderController(repo, security)

    auth.register("alice", "password123")

    product_ctrl.add_product(1, "Laptop", 1000)

    injection_attack(product_ctrl)  # should FAIL

    product = product_ctrl.get_product(1)
    order_ctrl.create_order("alice", product, 1)

    # Insecure mode
    print("\n=== INSECURE MODE ===")

    repo2 = DataRepository()
    security2 = SecurityConfig(False)

    auth2 = AuthController(repo2, security2)
    product_ctrl2 = ProductController(security2)
    order_ctrl2 = OrderController(repo2, security2)

    auth2.register("alice", "password123")

    product_ctrl2.add_product(1, "Laptop", 1000)

    injection_attack(product_ctrl2)  # should PASS

    product2 = product_ctrl2.get_product(1)
    order_ctrl2.create_order("alice", product2, 1)


if __name__ == "__main__":
    test_system()
