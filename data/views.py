from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from rest_framework.response import Response

# Create your views here.


class ContactsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        all_users = User.objects.all()
        all_contacts = UserSerializer(all_users, many=True)
        return Response(all_contacts.data)
