from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
    
    
class Contacts2View(APIView):
    pass