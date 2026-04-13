class SecurityStrategy:
"""Abstract base for all security behaviours.
Defines the contract used by the controller."""


    def validate_input(self, data: str) -> bool:
        raise NotImplementedError

    def apply_rate_limit(self, user: str) -> bool:
        raise NotImplementedError

    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    def log_event(self, message: str) -> None:
        raise NotImplementedError
