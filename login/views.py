from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .utils import *


class LoginView(ObtainAuthToken):
    """
    Custom view for handling user login.

    Inherits:
        ObtainAuthToken: Django Rest Framework's ObtainAuthToken class for token-based authentication.

    Methods:
        post(self, request, *args, **kwargs): Handles POST requests for user login.

    """
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests for user login.

        Parameters:
            request (Request): A Django request object containing user login credentials.

        Returns:
            Response: A Django Rest Framework response containing login success or failure information.

        """    
        try:
            request.data['username'] = get_username_by_email(request)
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, create = Token.objects.get_or_create(user=user)
            return Response(login_successful(user, token))
        except:
            return Response(login_failed())
        
        