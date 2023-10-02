from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username=models.CharField(max_length=10,  unique=True)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    user_bio=models.CharField(max_length=50)
    author_profile= models.ImageField(upload_to= "images/")
    user_description=models.TextField(max_length=50)   
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= []
    objects = UserManager()

    def __str__(self):
        return self.username
    
