import os
import django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Test users setup
        cls.admin_user = User.objects.create_user(username='admin_user', password='admin_pass')
        cls.student_user = User.objects.create_user(username='student_user', password='student_pass')

    def test_login_as_admin(self):
        response = self.client.post(reverse('login'), {'username': 'admin_user', 'password': 'admin_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Dashboard')  # Modify according to your app

    def test_login_as_student(self):
        response = self.client.post(reverse('login'), {
            'username': 'student_user',
            'password': 'student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Dashboard')  # Modify according to your app

    def test_login_as_non_admin(self):
        response = self.client.post(reverse('login'), {
            'username': 'non_admin',
            'password': 'non_admin_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Ensure non-admin cannot access admin dashboard

    def test_login_as_non_student(self):
        response = self.client.post(reverse('login'), {
            'username': 'non_student',
            'password': 'non_student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Student Dashboard')  # Ensure non-student cannot access student dashboard

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'invalid_user',
            'password': 'wrong_pass'
        })
        self.assertEqual(response.status_code, 401)  # Assuming 401 indicates unauthorized
        self.assertContains(response, 'Invalid credentials')  # Modify according to your app
