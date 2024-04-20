from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .utils import *


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user registration.

        Parameters:
        - request: The HTTP request object containing user registration data.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: A JSON response indicating the result of the registration process.
            If the registration is successful, it returns {'error': 'none'}.
            If the provided email is already registered, it returns {'error': 'Email already registered'}.
            If the passwords provided do not match, it returns {'error': 'Passwords do not match'}.
        """
        user_dic = create_user_dic(request)
        if request.data.get("password") == request.data.get("cPassword"):
            if User.objects.filter(email=request.POST.get("email")).exists():
                return Response({"error": "Email already registered"})
            else:
                user = User.objects.create(**user_dic)
                user.set_password(user_dic["password"])
                user.save()
                create_Contact(user.pk)
                return Response({"error": "none"})
        else:
            return Response({"error": "Passwords do not match"})
