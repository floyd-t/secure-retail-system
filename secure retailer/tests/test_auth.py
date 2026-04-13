from data.repository import DataRepository
from security.security_config import SecurityConfig
from controllers.auth_controller import AuthController
from attacks.brute_force import brute_force_attack

def run_attack_demo():
    # Secure mode
    print("=== SECURE MODE ===")
    repo_secure = DataRepository()
    secure_config = SecurityConfig(secure_mode=True)
    auth_secure = AuthController(repo_secure, secure_config)

    # Register user
    auth_secure.register("alice", "password123")

    # Run attack
    brute_force_attack(auth_secure, "alice")

    # Insecure mode
    print("\n=== INSECURE MODE ===")
    repo_insecure = DataRepository()
    insecure_config = SecurityConfig(secure_mode=False)
    auth_insecure = AuthController(repo_insecure, insecure_config)

    # Register user again
    auth_insecure.register("alice", "password123")

    # Run attack but insecure
    brute_force_attack(auth_insecure, "alice")


if __name__ == "__main__":
    run_attack_demo()
