class DataRepository:

    def __init__(self):
        # Username → customer object
        self.users = {}

        # List of order objects
        self.orders = []

        # Active session tokens
        self.sessions = set()

    def add_user(self, username, customer):
        # Store a new user in dictionary
        self.users[username] = customer

    def get_user(self, username):
        # Retrieve user
        return self.users.get(username)

    def add_order(self, order):
        # Append order to list
        self.orders.append(order)

    def get_orders(self):
        # Return all orders
        return self.orders

    def add_session(self, token):
        # Stores active session token
        self.sessions.add(token)

    def is_valid_session(self, token):
        # Check session existence
        return token in self.sessions

    def remove_session(self, token):
        # Invalidate session
        self.sessions.discard(token)
