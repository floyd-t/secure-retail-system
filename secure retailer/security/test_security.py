from security.security_config import SecurityConfig


def test_security_modes():
    secure = SecurityConfig(secure_mode=True)
    insecure = SecurityConfig(secure_mode=False)

    print("SECURE HASH:", secure.strategy.hash_password("password"))
    print("INSECURE HASH:", insecure.strategy.hash_password("password"))

    print("SECURE VALID:", secure.strategy.validate_input("DROP TABLE"))
    print("INSECURE VALID:", insecure.strategy.validate_input("DROP TABLE"))


if __name__ == "__main__":
    test_security_modes()
