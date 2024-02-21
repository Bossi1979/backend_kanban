from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from register.utils import create_background_color
from .serializer import ContactsSerializer
from rest_framework.response import Response
from .models import AddTaskItem, ContactsItem


# Create your views here.


class ContactsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        contacts = ContactsItem.objects.all().order_by('lastname')
        all_contacts = ContactsSerializer(contacts, many=True)
        return Response(all_contacts.data)

class AddTaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        task_data = request.data
        title = task_data['title']
        description = task_data['description']
        category = task_data['category']
        subtask = task_data['subtask']
        due_date = task_data['dueDate']
        prio=task_data['prio']
        assigned_to = task_data['assignTo']
        processing_status = task_data['processingStatus']
        
        newTask = AddTaskItem.objects.create(title=title, description=description, category=category, subtask=subtask, due_date=due_date, prio=prio, assigned_to=assigned_to, processing_status=processing_status) 
        return Response(task_data)
    
    
class AddContactView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        username = request.data['username']
        email = request.data['email']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        name_abbreviation = request.data['nameAbbreviation']
        background_color = create_background_color(firstname[0], lastname[0])
        checked = request.data['checked']
        phone = request.data['phone']
        has_account = request.data['hasAccount']
        contact = ContactsItem.objects.create(
            username = username,
            email = email,
            firstname = firstname,
            lastname = lastname,
            name_abbreviation = name_abbreviation,
            background_color = background_color,
            checked = checked,
            phone = phone,
            has_account = has_account,
        )
        
        contacts = ContactsItem.objects.all().order_by('lastname')
        all_contacts = ContactsSerializer(contacts, many=True)
        return Response(all_contacts.data)
       
        
        