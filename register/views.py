from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(APIView):
    
    def post(self, request, *args, **kwargs):
        firstname = request.data.get('firstname')
        lastname = request.data.get('lastname')
        email = request.data.get('email')
        password = request.data.get('password')
        c_password = request.data.get('cPassword')
        username = request.data.get('username')
        if password == c_password:
            if User.objects.filter(email=request.POST.get('email')).exists():
                print('User already registered')
                return Response({'error': 'Email already registered'})
            else:
                user = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email)
                user.set_password(password)
                user.save()
                return Response({'error': 'none'})
        else:
            return Response({'error': 'Passwords do not match'})