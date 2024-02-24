from django.shortcuts import render
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
