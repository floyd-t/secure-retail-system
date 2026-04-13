def injection_attack(product_controller):

    # Simulates attack via product input
    malicious_input = "DROP TABLE users;"

    print("\nAttempting injection attack...\n")

    success = product_controller.add_product(
        product_id=999,
        name=malicious_input,
        price=100
    )

    print("Injection accepted?" , success)