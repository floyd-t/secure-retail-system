import hashlib
import time

class SecureStrategy:
    def __init__(self):
        # Tracks login attempts per user
        self.login_attempts = {}

        # Tracks locked accounts
        self.locked_accounts = set()

        # Configuration
        self.MAX_ATTEMPTS = 5
        self.WINDOW_SECONDS = 10

    def validate_input(self, data: str) -> bool:
        # Blocks common injection patterns
        forbidden_patterns = ["'", "\"", ";", "--", "DROP", "SELECT"]
        return not any(pattern in data.upper() for pattern in forbidden_patterns)

    def apply_rate_limit(self, user: str) -> bool:

        # If already locked, blocks instantly
        if user in self.locked_accounts:
            return False

        now = time.time()
        attempts = self.login_attempts.get(user, [])
        attempts = [t for t in attempts if now - t < self.WINDOW_SECONDS]

        # Add current attempt to count
        attempts.append(now)
        self.login_attempts[user] = attempts

        # Locks account if too many attempts
        if len(attempts) >= self.MAX_ATTEMPTS:
            self.locked_accounts.add(user)
            return False

        return True

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def log_event(self, message: str) -> None:
        print(f"[SECURE LOG] {message}")