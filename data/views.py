from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView

# from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import ContactsSerializer
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


class AddContactView(APIView):
    """
    A view for adding a new contact.
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
