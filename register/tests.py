from django.test import TestCase
from .utils import *

# Create your tests here.

class SignupTestCase(TestCase):
    signup_test_data = {
            'firstname': 'John', 
            'lastname': 'Doe', 
            'email': 'testuser@test.de',
            'password': 'test_password',
            'cPassword': 'test_password',
            'username': 'John Doe',
            }
    def test_create_signup(self):
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.status_code, 200)
        
    def test_create_signup_email_already_exist(self):
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@test.de')
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.data, {'error': 'Email already registered'})
        
    def test_passwords_not_equal(self):
        self.signup_test_data['cPassword'] = 'not_equal_password'
        response = self.client.post('/register/', self.signup_test_data)
        self.assertEqual(response.data, {'error': 'Passwords do not match'})
