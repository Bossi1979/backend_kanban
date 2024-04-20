from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import AddTaskItem, ContactsItem


class TestModels(TestCase):
    """
    Test cases for model classes.
    """
    test_contact_data = {
        'id_user': 1,
        'username': 'John Doe',
        'email':  'john@doe.com',
        'firstname': 'John',
        'lastname':  'Doe',
        'name_abbreviation':  'JD',
        'phone':  '0815',
        'background_color':  '#582234',
        'checked': False,
        'has_account': False,
    }
    new_task_data = {
        'title': 'Test Task',
        'description': 'Test Task Description',
        'assigned_to': '[]',
        'due_date': '20/04/2025',
        'category': 'Technical Task',
        'subtask': '[]',
        'prio': 1,
        'processing_status': 0,
    }
    
    
    def test_model_contacts_item(self):
        """
        Test ContactsItem model creation.

        Creates a ContactsItem instance with test data and asserts that the instance
        is of the correct type and has the correct attributes.
        """
        contact_item = ContactsItem.objects.create(**self.test_contact_data)
        self.assertTrue(isinstance(contact_item, ContactsItem))
        self.assertEqual(contact_item.id_user, self.test_contact_data['id_user'])
        self.assertEqual(contact_item.username, self.test_contact_data['username'])
        self.assertEqual(contact_item.firstname, self.test_contact_data['firstname'])
        self.assertEqual(contact_item.lastname, self.test_contact_data['lastname'])
        self.assertEqual(contact_item.email, self.test_contact_data['email'])
        self.assertEqual(contact_item.name_abbreviation, self.test_contact_data['name_abbreviation'])
        self.assertEqual(contact_item.phone, self.test_contact_data['phone'])
        self.assertEqual(contact_item.background_color, self.test_contact_data['background_color'])
        self.assertEqual(contact_item.checked, self.test_contact_data['checked'])
        self.assertEqual(contact_item.has_account, self.test_contact_data['has_account'])
        
        
    def test_model_add_task_item(self):
        """
        Test AddTaskItem model creation.

        Creates an AddTaskItem instance with test data and asserts that the instance
        is of the correct type and has the correct attributes.
        """
        task_item = AddTaskItem.objects.create(**self.new_task_data)
        self.assertTrue(isinstance(task_item, AddTaskItem))
        self.assertEqual(task_item.title, self.new_task_data['title'])
        self.assertEqual(task_item.description, self.new_task_data['description'])
        self.assertEqual(task_item.assigned_to, self.new_task_data['assigned_to'])
        self.assertEqual(task_item.due_date, self.new_task_data['due_date'])
        self.assertEqual(task_item.category, self.new_task_data['category'])
        self.assertEqual(task_item.subtask, self.new_task_data['subtask'])
        self.assertEqual(task_item.prio, self.new_task_data['prio'])
        self.assertEqual(task_item.processing_status, self.new_task_data['processing_status'])
        

class ContactTestCase(TestCase):
    """
    Test case for contact-related operations.
    """
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
        """
        Create a test user and authenticate client with a token.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


    def test_create_contact(self):
        """
        Test creating a new contact.

        Creates a test user, sends a POST request to create a contact,
        and asserts that the contact is created successfully.
        """
        self.create_test_user()
        response = self.client.post("/contacts/", self.contact_data)
        self.assertEqual(response.data[0]["username"], "John Doe")
        self.assertEqual(response.data[0]["background_color"], "#582234")
        self.assertEqual(response.status_code, 200)


    def test_get_all_contact(self):
        """
        Test retrieving all contacts.

        Creates a test user, sends a GET request to retrieve all contacts,
        and asserts that the request is successful.
        """
        self.create_test_user()
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)


    def test_get_all_contact_without_auth(self):
        """
        Test retrieving all contacts without authentication.

        Sends GET requests to retrieve all contacts without authentication
        and asserts that the requests return status code 401 (Unauthorized).
        """
        response_get = self.client.get("/contacts/")
        response_post = self.client.get("/contacts/")
        self.assertEqual(response_get.status_code, 401)
        self.assertEqual(response_post.status_code, 401)


    def test_update_contact(self):
        """
        Test updating a contact.

        Creates a test user and a contact, sends a PATCH request to update
        the contact, and asserts that the contact is updated successfully.
        """
        self.create_test_user()
        response_created_contact = self.client.post("/contacts/", self.contact_data)
        response_updated_contact = self.client.patch(
            "/contacts/", self.updated_contact_data
        )
        self.assertEqual(response_created_contact.status_code, 200)
        self.assertEqual(response_updated_contact.data[0]["phone"], "0815")
        self.assertEqual(response_updated_contact.status_code, 200)


    def test_delete_contact(self):
        """
        Test deleting a contact.

        Creates a test user and a contact, sends a DELETE request to delete
        the contact, and asserts that the contact is deleted successfully.
        """
        self.create_test_user()
        self.client.post("/contacts/", self.contact_data)
        contacts = ContactsItem.objects.all()
        self.assertEqual(len(contacts), 1)
        response_delete_contact = self.client.delete("/contacts/1/")
        self.assertEqual(response_delete_contact.status_code, 200)


class AddTasksTestCase(TestCase):
    """
    Test case for task-related operations.
    """
    new_task_data = {
        'title': 'Test Task',
        'description': 'Test Task Description',
        'assignTo': '[]',
        'dueDate': '20/04/2025',
        'category': 'Technical Task',
        'subtask': '[]',
        'prio': 1,
        'processingStatus': 0,
        'id': 1,
    }
    updated_task_data = {
        'title': 'Test Task 1',
        'description': 'Test Task Description',
        'assignTo': '[]',
        'dueDate': '20/04/2026',
        'category': 'Technical Task',
        'subtask': '[]',
        'prio': 1,
        'processingStatus': 0,
        'id': 1,
    }
    
    
    def create_test_user(self):
        """
        Create a test user and authenticate client with a token.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", password="password", email="testuser@test.de"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


    def test_create_new_task(self):
        """
        Test creating a new task.

        Creates a test user, sends a POST request to create a task,
        and asserts that the task is created successfully.
        """
        self.create_test_user()
        response = self.client.post("/add_task/", self.new_task_data)
        self.assertEqual(response.status_code, 200)
    
    
    def test_get_all_tasks(self):
        """
        Test retrieving all tasks.

        Creates a test user, sends a GET request to retrieve all tasks,
        and asserts that the request is successful.
        """
        self.create_test_user()
        response = self.client.get("/add_task/")
        self.assertEqual(response.status_code, 200)
        
        
    def test_update_task(self):
        """
        Test updating a task.

        Creates a test user and a task, sends a PATCH request to update
        the task, and asserts that the task is updated successfully.
        """
        self.create_test_user()
        self.client.post("/add_task/", self.new_task_data)
        response = self.client.patch("/add_task/", self.updated_task_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'task updated successfully'})
        
        
    def test_delete_task(self):
        """
        Test deleting a task.

        Creates a test user and a task, sends a DELETE request to delete
        the task, and asserts that the task is deleted successfully.
        """
        self.create_test_user()
        self.client.post("/add_task/", self.new_task_data)
        response = self.client.delete('/add_task/1/')
        self.assertEqual(response.status_code, 200)
        
        
