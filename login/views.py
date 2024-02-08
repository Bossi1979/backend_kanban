from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):    
        email = request.data.get('email')
        user = User.objects.get(email=email)
        if user:
            print('user found')
        else:
            print('user not found')
        request.data['username'] = user.username
        serializer = self.serializer_class(data=request.data, context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, create = Token.objects.get_or_create(user=user)
            return Response({
            'username': user.username,
            'email': user.email,
            'token': token.key,
            'error': 'none'
        })
        except:
            return Response(
                {
                    'error': 'Login data not corect !'
                }
            )
        