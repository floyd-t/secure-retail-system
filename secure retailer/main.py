from data.repository import DataRepository
from security.security_config import SecurityConfig
from controllers.auth_controller import AuthController
from controllers.product_controller import ProductController
from controllers.order_controller import OrderController
from attacks.brute_force import brute_force_attack
from attacks.injection import injection_attack


def main():

    # Main CLI setup

    # Initial system setup
    repo = DataRepository()
    security = SecurityConfig(True)  # default = secure mode ON

    auth = AuthController(repo, security)
    product_ctrl = ProductController(security)
    order_ctrl = OrderController(repo, security)

    current_user = None

    # Preload product (so system is usable immediately)
    product_ctrl.add_product(1, "Laptop", 1000)

    while True:
        print("\n=== SECURE ONLINE RETAILER ===")
        print(f"Security Mode: {'ON' if security.secure_mode else 'OFF'}")

        print("\n1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Place Order")
        print("5. Toggle Security Mode")
        print("6. Run Brute Force Attack")
        print("7. Run Injection Attack")
        print("0. Exit")

        choice = input("Select option: ")

        # Register
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            success = auth.register(username, password)
            print("Registered." if success else "Registration failed.")

        # Login
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")

            token = auth.login(username, password)

            if token:
                current_user = username
                print("Login successful.")
            else:
                print("Login failed.")

        # View products
        elif choice == "3":
            product_ctrl.list_products()

        # Place order
        elif choice == "4":
            if not current_user:
                print("You must login first.")
                continue

            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))

            product = product_ctrl.get_product(product_id)

            if not product:
                print("Invalid product.")
                continue

            order_ctrl.create_order(current_user, product, quantity)

        # Toggle security
        elif choice == "5":
            security.toggle()
            print("Security mode toggled.")

        # Brute force attack
        elif choice == "6":
            username = input("Target username: ")
            brute_force_attack(auth, username)

        # Injection attack
        elif choice == "7":
            injection_attack(product_ctrl)

        # Exit
        elif choice == "0":
            print("Exiting system.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
