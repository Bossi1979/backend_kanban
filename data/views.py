from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import AddTaskSerializer, ContactsSerializer
from rest_framework.response import Response
from .models import AddTaskItem, ContactsItem
from .utils import create_task_dic, create_contact_dic


class ContactsView(APIView):
    """
    A view for handling contacts data retrieval.
    Requires token authentication.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        """
        Handles POST requests to add a new contact.

        Args:
            request (HttpRequest): The request object containing contact data.
            format (str, optional): The requested format. Defaults to None.

        Returns:
            Response: A response containing data of all contacts.
        """
        contact_dic = create_contact_dic(request.data)
        ContactsItem.objects.create(**contact_dic)
        contacts = ContactsItem.objects.all().order_by("lastname")
        all_contacts = ContactsSerializer(contacts, many=True)
        return Response(all_contacts.data)

    def get(self, request, format=None):
        """
        Handles GET requests to retrieve all contacts.

        Args:
            request (HttpRequest): The request object.
            format (str, optional): The requested format. Defaults to None.

        Returns:
            Response: A response containing data of all contacts.
        """
        contacts = ContactsItem.objects.all().order_by("lastname")
        all_contacts = ContactsSerializer(contacts, many=True)
        return Response(all_contacts.data)

    def delete(self, request, contact_id):
        """
            Delete a contact.

        Parameters:
        - request: The HTTP request object.
        - contact_id: The ID of the contact to be deleted.

        Returns:
        - Response: A JSON response indicating the result of the operation.
            If the contact is deleted successfully, it returns {"error": "none"}.
            If the contact cannot be deleted due to having an associated account, it returns {"message": "failed"}.
        """
        contact_obj = ContactsItem.objects.get(id=contact_id)
        if contact_obj.has_account == False:
            ContactsItem.objects.filter(id=contact_id).delete()
            return Response({"error": "none"})
        else:
            return Response({"message": "failed"})

    def patch(self, request, format=None):
        """
        Handle PATCH requests for updating a contact.

        This method is responsible for processing PATCH requests to update an existing contact.
        It retrieves the contact ID from the request data, fetches the corresponding contact object,
        updates its data based on the provided request data, saves the changes to the database,
        retrieves all contacts sorted by last name, serializes them, and returns the serialized
        data as a response.

        Parameters:
        - request (HttpRequest): The PATCH request object containing the updated contact data.
        - format (str): The requested format of the response data. Default is None.

        Returns:
        - Response: A response containing serialized data of all contacts sorted by last name.

        Raises:
        - Http404: If the requested contact does not exist.
        - Exception: If an error occurs during the update process.

        Example:
        >>> # Sample PATCH request data:
        >>> # {
        >>> #     "id": 123,
        >>> #     "firstname": "John",
        >>> #     "lastname": "Doe",
        >>> #     "email": "john.doe@example.com",
        >>> #     "phone": "1234567890"
        >>> # }
        >>> # Sample PATCH request:
        >>> # PATCH /contacts/123
        >>> # Response status: 200 OK
        >>> # Response data: Serialized data of all contacts after updating
        """
        contact_id = request.data["id"]
        editContact = get_object_or_404(ContactsItem, id=contact_id)
        updated_contact_data = create_contact_dic(request.data)
        for key, value in updated_contact_data.items():
            setattr(editContact, key, value)
        editContact.save()
        contacts = ContactsItem.objects.all().order_by("lastname")
        all_contacts = ContactsSerializer(contacts, many=True)
        return Response(all_contacts.data)


class AddTaskView(APIView):
    """
    A view for adding a new task.
    Requires token authentication.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        """
        Handles POST requests to add a new task.

        Args:
            request (HttpRequest): The request object containing task data.
            format (str, optional): The requested format. Defaults to None.

        Returns:
            Response: A response containing the newly created task data.
        """
        task_dic = create_task_dic(request.data)
        newTask = AddTaskItem.objects.create(**task_dic)
        return Response(task_dic)

    def get(self, request, format=None):
        """
        Retrieve all tasks.

        Parameters:
        - request: The HTTP request object.
        - format (optional): The format of the response data.

        Returns:
        - Response: A JSON response containing the serialized data of all tasks.
        """

        """
        To return only the tasks that are assigned to the logged user or has no assigned member, 
        activate the to lines:
        
        user_id = request.user.id
        all_tasks = AddTaskSerializer(filter_assigned_to_logged_user(user_id), many=True)
        
        and deactivated:
        
        tasks = AddTaskItem.objects.all()
        all_tasks = AddTaskSerializer(tasks, many=True)
        
        """
        # user_id = request.user.id
        # all_tasks = AddTaskSerializer(filter_assigned_to_logged_user(user_id), many=True)

        tasks = AddTaskItem.objects.all()
        all_tasks = AddTaskSerializer(tasks, many=True)
        return Response(all_tasks.data)
    

    def patch(self, request, format=None):
        """
        Update a task partially.

        Parameters:
        - request: The HTTP request object containing the updated task data.
        - format (optional): The format of the response data.

        Returns:
        - Response: A JSON response indicating the successful update of the task.
        """
        task_id = request.data["id"]
        task = get_object_or_404(AddTaskItem, id=task_id)
        task_dic = create_task_dic(request.data)
        for key, value in task_dic.items():
            setattr(task, key, value)
        task.save()
        return Response({"message": "task updated successfully"})
    

    def delete(self, request, task_id):
        """
        Delete a task.

        Parameters:
        - request: The HTTP request object.
        - task_id: The ID of the task to be deleted.

        Returns:
        - Response: A JSON response indicating the successful deletion of the task.
        """
        task_obj = get_object_or_404(AddTaskItem, id=task_id)
        task_obj.delete()
        return Response({"message": "Task deleted successfully"})
