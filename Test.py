import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')  # Replace 'my_project.settings' with your actual settings module

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up initial data for the tests."""
        # Create test users with valid credentials
        cls.admin_user = User.objects.create_user(username='Mohamed Hossam', password='P@ss01451')
        cls.student_user = User.objects.create_user(username='Seif Kassab', password='Ardonia19#sk')
        cls.non_admin_user = User.objects.create_user(username='Ranim Hisham', password='Tr19$sk20')
        cls.non_student_user = User.objects.create_user(username='Farida Amr', password='Ytq71k@fa')
        cls.extra_user = User.objects.create_user(username='Karim Zaky', password='Kym895!zk')

    def test_login_as_admin_valid(self):
        """Test login functionality for an admin user with valid credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'Mohamed Hossam',
            'password': 'P@ss01451'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Dashboard')  # Replace with actual dashboard content

    def test_login_as_admin_invalid_user(self):
        """Test login functionality for an admin user with invalid credentials."""
        # Use "Ranim Hisham" (non-admin user) as the username instead of admin
        response = self.client.post(reverse('login'), {
            'username': 'Ranim Hisham',
            'password': 'P@ss01451'  # Admin's password
        })
        # Check that login fails
        self.assertEqual(response.status_code, 401)  # Adjust the status code based on your app's behavior
        self.assertContains(response, 'Invalid credentials')  # Replace with your app's error message

    def test_login_as_student_valid(self):
        """Test login functionality for a student user with valid credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'Seif Kassab',
            'password': 'Ardonia19#sk'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Dashboard')  # Replace with actual dashboard content

    def test_login_as_student_invalid_user(self):
        """Test login functionality for a student user with invalid credentials."""
        # Use "Farida Amr" (non-student user) as the username instead of student
        response = self.client.post(reverse('login'), {
            'username': 'Farida Amr',
            'password': 'Ardonia19#sk'  # Student's password
        })
        # Check that login fails
        self.assertEqual(response.status_code, 401)  # Adjust based on your app's behavior
        self.assertContains(response, 'Invalid credentials')  # Replace with your app's error message

    def test_login_as_non_admin_valid(self):
        """Test login functionality for a non-admin user."""
        # Use valid non-admin credentials
        response = self.client.post(reverse('login'), {
            'username': 'Ranim Hisham',
            'password': 'Tr19$sk20'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Ensure no access to admin content

    def test_login_as_non_student_invalid(self):
        """Test login functionality for a non-student user with invalid credentials."""
        # Use mismatched credentials where the admin's username is paired with a non-student's password
        response = self.client.post(reverse('login'), {
            'username': 'Mohamed Hossam',  # Admin user
            'password': 'Ytq71k@fa'  # Password of non-student user
        })
        self.assertEqual(response.status_code, 401)  # Adjust based on your app's behavior
        self.assertContains(response, 'Invalid credentials')  # Replace with your app's error message

    def test_login_with_invalid_credentials(self):
        """Test login functionality with completely invalid credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'Invalid User',
            'password': 'WrongPassword'
        })
        self.assertEqual(response.status_code, 401)  # Assuming 401 indicates unauthorized
        self.assertContains(response, 'Invalid credentials')  # Replace with your app's error message

