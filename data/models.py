from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class AddTaskItem(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  category = models.CharField(max_length=100)
  subtask = models.CharField(max_length=100)
  due_date = models.CharField(max_length=10)
  prio=models.CharField(max_length=1)
  assigned_to = models.JSONField(default=list)
  
  
  



