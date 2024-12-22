import os
import django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Set the settings module explicitly
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
django.setup()  # Setup Django

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up test data that is shared across tests. 
        This method is run only once for all tests.
        """
        # Create users for testing
        cls.admin_user = User.objects.create_user(username='admin_user', password='admin_pass')
        cls.student_user = User.objects.create_user(username='student_user', password='student_pass')
        cls.non_admin_user = User.objects.create_user(username='non_admin', password='non_admin_pass')
        cls.non_student_user = User.objects.create_user(username='non_student', password='non_student_pass')

        # Assign groups or roles if needed
        # Example: cls.admin_user.groups.add(Group.objects.get(name='Admin'))

    def test_login_as_admin(self):
        """
        Test login for admin user
        """
        response = self.client.post(reverse('login'), {
            'username': 'admin_user',
            'password': 'admin_pass'
        })
        self.assertEqual(response.status_code, 200)  # Assuming 200 indicates success
        self.assertContains(response, 'Admin Dashboard')  # Modify according to your app's response

    def test_login_as_student(self):
        """
        Test login for student user
        """
        response = self.client.post(reverse('login'), {
            'username': 'student_user',
            'password': 'student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Dashboard')  # Modify according to your app's response

    def test_login_as_non_admin(self):
        """
        Test login for a non-admin user and ensure they can't access the admin dashboard
        """
        response = self.client.post(reverse('login'), {
            'username': 'non_admin',
            'password': 'non_admin_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Ensure non-admin cannot access admin dashboard

    def test_login_as_non_student(self):
        """
        Test login for a non-student user and ensure they can't access the student dashboard
        """
        response = self.client.post(reverse('login'), {
            'username': 'non_student',
            'password': 'non_student_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Student Dashboard')  # Ensure non-student cannot access student dashboard

    def test_login_with_invalid_credentials(self):
        """
        Test login with invalid credentials
        """
        response = self.client.post(reverse('login'), {
            'username': 'invalid_user',
            'password': 'wrong_pass'
        })
        self.assertEqual(response.status_code, 401)  # Assuming 401 indicates unauthorized
        self.assertContains(response, 'Invalid credentials')  # Modify according to your app's response

if __name__ == "__main__":
    # Execute the test suite
    from django.test import TestRunner
    runner = TestRunner()
    runner.run(LoginTestCase)
