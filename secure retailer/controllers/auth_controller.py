import uuid
# Used to generate unique session tokens

class AuthController:
    # Handles authentication, registration and session management

    def __init__(self, repository, security_config):
        self.repo = repository
        self.security = security_config

    def register(self, username, password):

        # Validates input and blocks injection in secure mode
        if not self.security.strategy.validate_input(username):
            self.security.strategy.log_event("Invalid username input detected")
            return False

        if self.repo.get_user(username):
            print("User already exists.")
            return False

        # Hash password
        password_hash = self.security.strategy.hash_password(password)

        from models.customer import Customer
        user = Customer(username, password_hash)

        self.repo.add_user(username, user)

        self.security.strategy.log_event(f"User registered: {username}")
        return True

    def login(self, username, password):
        # Authenticate a user and create a session

        # Rate limiting check
        if not self.security.strategy.apply_rate_limit(username):
            self.security.strategy.log_event(f"Rate limit exceeded for {username}")
            print("Too many login attempts. Try again later.")
            return None

        user = self.repo.get_user(username)

        if not user:
            self.security.strategy.log_event(f"Login failed (no user): {username}")
            return None

        password_hash = self.security.strategy.hash_password(password)

        if not user.verify_password(password_hash):
            self.security.strategy.log_event(f"Login failed (wrong password): {username}")
            return None

        # Create session token
        token = str(uuid.uuid4())
        self.repo.add_session(token)

        self.security.strategy.log_event(f"User logged in: {username}")
        return token

    # Session validation check

    def is_authenticated(self, token):
        return self.repo.is_valid_session(token)

    # Logout

    def logout(self, token):
        self.repo.remove_session(token)
        self.security.strategy.log_event("User logged out")