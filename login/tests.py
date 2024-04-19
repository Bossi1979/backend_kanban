from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from django.urls import reverse

from django.contrib.auth.models import User



# Create your tests here.

class LoginTestCase(TestCase):
    def test_login(self):
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@test.de')
        response = self.client.post('/login/', {'email': 'testuser@test.de', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        
    def test_failed_login(self):
        # Ungültige Anmeldeinformationen
        invalid_credentials = {
            'email': 'testuser@test.de',
            'password': 'wrong_password'
        }

        # Führen Sie eine POST-Anfrage für den Login-Vorgang mit ungültigen Anmeldeinformationen durch
        response = self.client.post('/login/', invalid_credentials)
        # Überprüfen, ob der Login fehlgeschlagen ist
        self.assertEqual(response.data, {"error": "Login failed"})
        self.assertEqual(response.status_code, 200)
        self.assertFalse('token' in response.data)  # Es sollte kein Token zurückgegeben werden

        
class LogoutTestCase(TestCase):
    def test_logout(self):
        # Erstelle einen Testbenutzer
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@test.de')
        self.token = Token.objects.create(user=self.user)
    
        # Authentifiziere den Client mit dem Token des Benutzers
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Führe deine Testfunktion durch, die den authentifizierten Client verwendet
        response = self.client.get('/logout/')  # Beispiel-Anfrage
    
        # Überprüfe die Antwort
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "logout successfully"})