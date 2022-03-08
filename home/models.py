import email
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Createtodo(models.Model):    
    title=models.CharField(max_length=100)
    memo=models.TextField()
    important=models.BooleanField(default=False)
    datecompleted=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title

class UserInformation(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pass1=models.CharField(max_length=1000)
    pass2=models.CharField(max_length=1000)

    def __str__(self):
        return self.username

