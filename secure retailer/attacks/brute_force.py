def brute_force_attack(auth_controller, username):

    # Simulates a brute force attack by trying many passwords
    passwords = ["1234", "password", "admin", "letmein", "qwerty", "password123"]

    print(f"\nStarting brute force attack on {username}...\n")

    for i, pwd in enumerate(passwords, start=1):
        token = auth_controller.login(username, pwd)

        if token:
            print(f"[Attempt {i}] SUCCESS with password: {pwd}")
            return
        else:
            print(f"[Attempt {i}] Failed: {pwd}")

    print("Attack finished. No successful login.")