import os
import django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')  # Replace 'my_project.settings' with your actual settings module
django.setup()  # Ensure Django apps are initialized before running tests

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up initial data for the tests."""
        # Create users for testing
        cls.admin_user = User.objects.create_user(username='admin_user', password='admin_pass')
        cls.student_user = User.objects.create_user(username='student_user', password='student_pass')
        cls.non_admin_user = User.objects.create_user(username='non_admin', password='non_admin_pass')
        cls.non_student_user = User.objects.create_user(username='non_student', password='non_student_pass')

    def test_login_as_admin(self):
        """Test login functionality for an admin user."""
        response = self.client.post(reverse('login'), {
            'username': 'admin_user',
            'password': 'admin_pass'
        })
        self.assertEqual(response.status_code, 200)  # Assuming 200 indicates success
        self.assertContains(response, 'Admin Dashboard')  # Replace with actual content in your app

    def test_login_as_student(self):
        """Test login functionality for a student user."""
        response = self.client.post(reverse('login'), {
            'username': 'student_user',
            'password': 'student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Dashboard')  # Replace with actual content in your app

    def test_login_as_non_admin(self):
        """Test login functionality for a non-admin user."""
        response = self.client.post(reverse('login'), {
            'username': 'non_admin',
            'password': 'non_admin_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Ensure non-admin users cannot access the admin dashboard

    def test_login_as_non_student(self):
        """Test login functionality for a non-student user."""
        response = self.client.post(reverse('login'), {
            'username': 'non_student',
            'password': 'non_student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Student Dashboard')  # Ensure non-students cannot access the student dashboard

    def test_login_with_invalid_credentials(self):
        """Test login functionality with invalid credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'invalid_user',
            'password': 'wrong_pass'
        })
        self.assertEqual(response.status_code, 401)  # Assuming 401 indicates unauthorized; replace with your app's behavior
        self.assertContains(response, 'Invalid credentials')  # Replace with the actual error message in your app
