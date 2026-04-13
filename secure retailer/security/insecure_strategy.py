class InsecureStrategy:
    """
    Intentionally weak security implementation.
    Used to demonstrate system vulnerability.
    """

    def validate_input(self, data: str) -> bool:
        return True  # No validation

    def apply_rate_limit(self, user: str) -> bool:
        return True  # No rate limiting

    def hash_password(self, password: str) -> str:
        return password  # Plain text

    def log_event(self, message: str) -> None:
        pass  # No logging