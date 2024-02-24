from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ContactsItem




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'first_name', 'last_name', 'id'
        
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsItem
        fields = 'id_user', 'username', 'email', 'firstname', 'lastname', 'name_abbreviation', 'background_color', 'checked', 'phone', 'has_account', 'id' 
