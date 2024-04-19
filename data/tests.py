from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from .models import AddTaskItem, ContactsItem


# Create your tests here.


class ContactTestCase(TestCase):
    contact_data = {
        "firstname": "John",
        "lastname": "Doe",
        "username": "John Doe",
        "email": "john@doe.com",
        "nameAbbreviation": "JD",
        "checked": False,
        "phone": "",
        "hasAccount": False,
    }

    updated_contact_data = {
        "firstname": "John",
        "lastname": "Doe",
        "username": "John Doe",
        "email": "john@doe.com",
        "nameAbbreviation": "JD",
        "checked": False,
        "phone": "0815",
        "hasAccount": False,
        "id": 1,
    }

    def create_test_user(self):
        # Erstelle einen Testbenutzer
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        self.token = Token.objects.create(user=self.user)
        # Authentifiziere den Client mit dem Token des Benutzers
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_contact(self):
        self.create_test_user()
        response = self.client.post("/contacts/", self.contact_data)
        self.assertEqual(response.data[0]["username"], "John Doe")
        self.assertEqual(response.data[0]["background_color"], "#582234")
        self.assertEqual(response.status_code, 200)

    def test_get_all_contact(self):
        self.create_test_user()
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)

    def test_get_all_contact_without_auth(self):
        response_get = self.client.get("/contacts/")
        response_post = self.client.get("/contacts/")
        self.assertEqual(response_get.status_code, 401)
        self.assertEqual(response_post.status_code, 401)

    def test_update_contact(self):
        self.create_test_user()
        response_created_contact = self.client.post("/contacts/", self.contact_data)
        response_updated_contact = self.client.patch(
            "/contacts/", self.updated_contact_data
        )
        self.assertEqual(response_created_contact.status_code, 200)
        self.assertEqual(response_updated_contact.data[0]["phone"], "0815")
        self.assertEqual(response_updated_contact.status_code, 200)

    def test_delete_contact(self):
        self.create_test_user()
        self.client.post("/contacts/", self.contact_data)
        contacts = ContactsItem.objects.all()
        self.assertEqual(len(contacts), 1)
        response_delete_contact = self.client.delete("/contacts/1/")
        self.assertEqual(response_delete_contact.status_code, 200)


class AddTasksTestCase(TestCase):
    new_task_data = {
        'title': 'Test Task',
        'description': 'Test Task Description',
        'assignTo': '[]',
        'dueDate': '20/04/2025',
        'category': 'Technical Task',
        'subtask': '[]',
        'prio': 1,
        'processingStatus': 0,
        'id': 0,
    }
    
    updated_task_data = {
        'title': 'Test Task 1',
        'description': 'Test Task Description',
        'assignTo': [],
        'dueDate': '20/04/2026',
        'category': 'Technical Task',
        'subtask': [],
        'prio': 1,
        'processingStatus': 0,
        'id': 0,
    }
    
    def create_test_user(self):
        # Erstelle einen Testbenutzer
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        self.token = Token.objects.create(user=self.user)
        # Authentifiziere den Client mit dem Token des Benutzers
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_new_task(self):
        self.create_test_user()
        response = self.client.post("/add_task/", self.new_task_data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_all_tasks(self):
        self.create_test_user()
        response = self.client.get("/add_task/")
        self.assertEqual(response.status_code, 200)
        
    # def test_update_task(self):
    #     self.create_test_user()
    #     response = self.client.post("/add_task/", self.new_task_data)
    #     self.assertEqual(response.status_code, 200)
        
    #     update_response = self.client.patch("/add_task/", self.updated_task_data)
    #     response_data = update_response.json()
    #     self.assertEqual(response_data['message'], 'task updated successfully')
    #     # self.assertEqual(update_response.status_code, 200)
        
        
