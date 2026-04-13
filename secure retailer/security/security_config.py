from security.secure_strategy import SecureStrategy
from security.insecure_strategy import InsecureStrategy
# Imports both secure and insecure strategies

class SecurityConfig:
    def __init__(self, secure_mode: bool = True):
        self.secure_mode = secure_mode
        self.strategy = self._select_strategy()

    def _select_strategy(self):
        if self.secure_mode:
            return SecureStrategy()
        return InsecureStrategy()

    def toggle(self):
        self.secure_mode = not self.secure_mode
        self.strategy = self._select_strategy()