from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    def test_login(self):
        """
        Test successful user login.

        Creates a new user, attempts to log in with valid credentials,
        and asserts that the login request returns a status code of 200.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        response = self.client.post(
            "/login/", {"email": "testuser@test.de", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)
        

    def test_failed_login(self):
        """
        Test failed user login with invalid credentials.

        Attempts to log in with invalid credentials and asserts that the login request
        returns a status code of 200 and an error message indicating login failure.
        """
        invalid_credentials = {
            "email": "testuser@test.de",
            "password": "wrong_password",
        }
        response = self.client.post("/login/", invalid_credentials)
        self.assertEqual(response.data, {"error": "Login failed"})
        self.assertEqual(response.status_code, 200)
        self.assertFalse("token" in response.data)


class LogoutTestCase(TestCase):
    def test_logout(self):
        """
        Test user logout.

        Creates a new user, logs in with valid credentials, performs a logout request,
        and asserts that the logout request returns a status code of 200 and a message
        indicating successful logout.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "logout successfully"})
