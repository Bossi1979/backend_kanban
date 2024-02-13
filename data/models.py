from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class AddTaskItem(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  category = models.CharField(max_length=100)
  subtask = models.JSONField(default=list)
  due_date = models.CharField(max_length=10)
  prio = models.IntegerField(default = 0)
  assigned_to = models.JSONField(default=list)
  processing_status = models.IntegerField(default = 0)
  

class ContactsItem(models.Model):
  id_user = models.IntegerField()
  username = models.CharField(max_length=50)
  email = models.CharField(max_length=100)
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  name_abbreviation = models.CharField(max_length=2)
  background_color = models.CharField(max_length=7)
  checked = models.BooleanField('', default=False)
  
  

  



