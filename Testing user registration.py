import unittest
from club_platform import UserFactory

class TestUserFactory(unittest.TestCase):
    def test_create_admin_user(self):
        admin = UserFactory.create_user("Admin", "Alice", "admin@example.com")
        self.assertEqual(admin.name, "Alice")
        self.assertEqual(admin.email, "admin@example.com")
        self.assertIsInstance(admin, Admin)

    def test_create_invalid_user(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("Invalid", "Bob", "bob@example.com")

if __name__ == "__main__":
    unittest.main()
