from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up the test data.
        """
        # Create admin user
        cls.admin_user = User.objects.create_user(
            username='Mohamed Hossam', 
            password='P@ss01451', 
            email='m.hossam2241@nu.edu.eg'
        )
        
        # Create student user
        cls.student_user = User.objects.create_user(
            username='Seif Kassab',
            password='Ardonia19#sk',
            email='s.Usama2251@nu.edu.eg'
        )

        # Create non-admin user
        cls.non_admin_user = User.objects.create_user(
            username='Ranim Hisham',
            password='Tr19$sk20',
            email='r.hisham2216@nu.edu.eg'
        )

        # Create non-student user
        cls.non_student_user = User.objects.create_user(
            username='Farida Amr',
            password='Ytq71k@fa',
            email='f.amr2237@nu.edu.eg'
        )
        
        # Create a user with invalid credentials
        cls.invalid_user = User.objects.create_user(
            username='Karim Zaky',
            password='Kym895!zk',
            email='k.zaky2190@nu.edu.eg'
        )

    def test_login_as_admin(self):
        """
        Test login with valid admin credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'Karim Zaky',
            'password': 'P@ss01451'
        })
        self.assertEqual(response.status_code, 200)  # Expect successful login
        self.assertContains(response, 'Admin Dashboard')  # Check for admin dashboard content

    def test_login_as_student(self):
        """
        Test login with valid student credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'Mohamed Hossam',
            'password': 'Ardonia19#sk'
        })
        self.assertEqual(response.status_code, 200)  # Expect successful login
        self.assertContains(response, 'Student Dashboard')  # Check for student dashboard content

    def test_login_as_non_admin(self):
        """
        Test login with valid non-admin credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'Farida',
            'password': 'Tr19$sk20'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Admin Dashboard')  # Ensure non-admin cannot access admin dashboard

    def test_login_as_non_student(self):
        """
        Test login with valid non-student credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'Kar',
            'password': 'Ytq71k@fa'
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Student Dashboard')  # Ensure non-student cannot access student dashboard

    def test_login_with_invalid_credentials(self):
        """
        Test login with invalid credentials.
        """
        response = self.client.post(reverse('login'), {
            'username': 'Karim Zaky',
            'password': 'Kym895!zk'
        })
        self.assertEqual(response.status_code, 401)  # Unauthorized status code for invalid credentials
        self.assertContains(response, 'Invalid credentials')  # Ensure invalid credentials message is shown
