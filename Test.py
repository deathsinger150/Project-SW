import os
import django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace 'your_project.settings' with the correct path
django.setup()

class UserLoginTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up initial data for the tests."""
        # Create test users
        cls.admin_user = User.objects.create_user(username='admin_user', password='admin_pass', is_staff=True)
        cls.student_user = User.objects.create_user(username='student_user', password='student_pass')
        cls.non_admin_user = User.objects.create_user(username='non_admin_user', password='non_admin_pass')
        cls.non_student_user = User.objects.create_user(username='non_student_user', password='non_student_pass')

    def test_login_as_admin(self):
        """Test login functionality for an admin user."""
        response = self.client.post(reverse('login'), {'username': 'admin_user', 'password': 'admin_pass'})
        self.assertEqual(response.status_code, 200)  # Ensure status code is correct
        # Adjust to check if the proper template or message is rendered
        self.assertContains(response, "Welcome Admin")

    def test_login_as_student(self):
        """Test login functionality for a student user."""
        response = self.client.post(reverse('login'), {'username': 'student_user', 'password': 'student_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome Student")

    def test_login_as_non_admin(self):
        """Test login functionality for a non-admin user."""
        response = self.client.post(reverse('login'), {'username': 'non_admin_user', 'password': 'non_admin_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome User")

    def test_login_as_non_student(self):
        """Test login functionality for a non-student user."""
        response = self.client.post(reverse('login'), {'username': 'non_student_user', 'password': 'non_student_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome Guest")

    def test_login_with_invalid_credentials(self):
        """Test login functionality with invalid credentials."""
        response = self.client.post(reverse('login'), {'username': 'invalid_user', 'password': 'wrong_pass'})
        self.assertEqual(response.status_code, 401)  # Adjust status code if your app uses a different one
        self.assertContains(response, "Invalid credentials")  # Adjust the error message if needed
