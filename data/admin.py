from django.contrib import admin
from .models import AddTaskItem
from data.models import ContactsItem

# Register your models here.
admin.site.register(AddTaskItem)
admin.site.register(ContactsItem)