from django.db import models

class User(models.Model): 
    user_name= models.CharField(max_length=64)
    user_email= models.EmailField(max_length=64)
    user_pw = models.CharField(max_length=64)