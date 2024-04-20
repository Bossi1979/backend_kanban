from django.test import TestCase
from .utils import *


class SignupTestCase(TestCase):
    """
    Test case for user signup functionality.
    """
    signup_test_data = {
            'firstname': 'John', 
            'lastname': 'Doe', 
            'email': 'testuser@test.de',
            'password': 'test_password',
            'cPassword': 'test_password',
            'username': 'John Doe',
            }
    def test_create_signup(self):
        """
        Test user signup with valid data.

        Sends a POST request to register a new user with valid data
        and asserts that the request is successful.
        """
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.status_code, 200)
        
    def test_create_signup_email_already_exist(self):
        """
        Test user signup with email already registered.

        Creates a user with the provided email, then sends a POST request
        to register a new user with the same email and asserts that the request
        returns an error message indicating that the email is already registered.
        """
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@test.de')
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.data, {'error': 'Email already registered'})
        
        
    def test_passwords_not_equal(self):
        """
        Test user signup with passwords not matching.

        Modifies the signup data to have mismatched passwords, then sends
        a POST request to register a new user and asserts that the request
        returns an error message indicating that the passwords do not match.
        """
        self.signup_test_data['cPassword'] = 'not_equal_password'
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.data, {'error': 'Passwords do not match'})
