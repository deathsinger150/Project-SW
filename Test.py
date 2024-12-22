import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up initial data for the tests."""
        cls.admin_user = User.objects.create_user(username='Mohamed Hossam', password='P@ss01451')
        cls.student_user = User.objects.create_user(username='Seif Kassab', password='Ardonia19#sk')
        cls.non_admin_user = User.objects.create_user(username='Ranim Hisham', password='Tr19$sk20')
        cls.non_student_user = User.objects.create_user(username='Farida Amr', password='Ytq71k@fa')
        cls.non_student_user = User.objects.create_user(username='Karim Zaky ', password='Kym895!zk')

    def test_login_as_admin(self):
        """Test login functionality for an admin user."""
        response = self.client.post(reverse('login'), {
            'username': 'Ranim Hisham',
            'password': 'P@ss01451'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Dashboard')  # Replace with actual dashboard content

    def test_login_as_student(self):
        """Test login functionality for a student user."""
        response = self.client.post(reverse('login'), {
            'username': 'Seif Kassab',
            'password': 'Ardonia19#sk'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Dashboard')  # Replace with actual dashboard content

    def test_login_as_non_admin(self):
        """Test login functionality for a non-admin user."""
        response = self.client.post(reverse('login'), {
            'username': 'Ranim Hisham',
            'password': 'Tr19$sk20'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Replace with actual non-admin content

    def test_login_as_non_student(self):
        """Test login functionality for a non-student user."""
        response = self.client.post(reverse('login'), {
            'username': 'Farida Amr',
            'password': 'Ytq71k@fa'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Student Dashboard')  # Replace with actual non-student content

    def test_login_with_invalid_credentials(self):
        """Test login functionality with invalid credentials."""
        response = self.client.post(reverse('login'), {
            'username': 'Karim Zaky',
            'password': 'Kym895!zk'
        })
        self.assertEqual(response.status_code, 200)  # Default behavior might return 200
        self.assertContains(response, 'Invalid credentials')  # Replace with your app's error message
