from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from rest_framework.response import Response
from .models import AddTaskItem

# Create your views here.


class ContactsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        all_users = User.objects.all()
        all_contacts = UserSerializer(all_users, many=True)
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
        
        newTask = AddTaskItem.objects.create(title=title, description=description, category=category, subtask=subtask, due_date=due_date, prio=prio, assigned_to=assigned_to) 
        return Response(task_data)