from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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

        
class LogoutView(APIView):
    """
    A view for handling user logout.
    Requires token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Handles GET requests for user logout.

    Args:
        request (HttpRequest): The request object.
        format (str, optional): The requested format. Defaults to None.

    Returns:
        Response: A response indicating the success of the logout operation.
    """
    
    
    def get(self, request, format=None):
        token = request.auth.pk
        token_entry = Token.objects.filter(key=token).first()
        logout(request)
        if token_entry:
            token_entry.delete()
        return Response({"message": "logout successfully"})