from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .utils import *

# Create your views here.


class RegisterView(APIView):
    
    def post(self, request, *args, **kwargs):
        user_dic = create_user_dic(request)
        if request.data.get('password') == request.data.get('cPassword'):
            if User.objects.filter(email=request.POST.get('email')).exists():
                return Response({'error': 'Email already registered'})
            else:
                user = User.objects.create(**user_dic)
                user.set_password(user_dic["password"])
                user.save()
                create_Contact(user.pk)
                return Response({'error': 'none'})
        else:
            return Response({'error': 'Passwords do not match'})
        
    


