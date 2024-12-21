from unittest import TestCase
from unittest.mock import patch
from django.contrib.auth import authenticate

class LoginUnitTestCase(TestCase):
    @patch('django.contrib.auth.authenticate')
    def test_login_as_admin(self, mock_authenticate):
        """Test login functionality for an admin user."""
        # Mock the authenticate response
        mock_authenticate.return_value = True
        
        user = authenticate(username='admin_user', password='admin_pass')
        self.assertTrue(user)
        mock_authenticate.assert_called_once_with(username='admin_user', password='admin_pass')

    @patch('django.contrib.auth.authenticate')
    def test_login_as_student(self, mock_authenticate):
        """Test login functionality for a student user."""
        mock_authenticate.return_value = True
        
        user = authenticate(username='student_user', password='student_pass')
        self.assertTrue(user)
        mock_authenticate.assert_called_once_with(username='student_user', password='student_pass')

    @patch('django.contrib.auth.authenticate')
    def test_login_as_non_admin(self, mock_authenticate):
        """Test login functionality for a non-admin user."""
        mock_authenticate.return_value = True
        
        user = authenticate(username='non_admin', password='non_admin_pass')
        self.assertTrue(user)
        mock_authenticate.assert_called_once_with(username='non_admin', password='non_admin_pass')

    @patch('django.contrib.auth.authenticate')
    def test_login_as_non_student(self, mock_authenticate):
        """Test login functionality for a non-student user."""
        mock_authenticate.return_value = True
        
        user = authenticate(username='non_student', password='non_student_pass')
        self.assertTrue(user)
        mock_authenticate.assert_called_once_with(username='non_student', password='non_student_pass')

    @patch('django.contrib.auth.authenticate')
    def test_login_with_invalid_credentials(self, mock_authenticate):
        """Test login functionality with invalid credentials."""
        mock_authenticate.return_value = None
        
        user = authenticate(username='invalid_user', password='wrong_pass')
        self.assertIsNone(user)
        mock_authenticate.assert_called_once_with(username='invalid_user', password='wrong_pass')
