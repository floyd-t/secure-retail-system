class Customer:

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def verify_password(self, password_hash):
        # Compare stored hash with provided hash
        return self.password_hash == password_hash
