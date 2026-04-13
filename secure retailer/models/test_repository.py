from data.repository import DataRepository
from models.customer import Customer


def test_repository():
    repo = DataRepository()

    # Create user
    user = Customer("alice", "hashed_pw")
    repo.add_user("alice", user)

    # Verify dictionary lookup
    retrieved = repo.get_user("alice")
    print("User retrieved:", retrieved.username)

    # Add session
    repo.add_session("token123")
    print("Session valid:", repo.is_valid_session("token123"))

    # Add order
    repo.add_order("ORDER_1")
    print("Orders:", repo.get_orders())


if __name__ == "__main__":
    test_repository() 