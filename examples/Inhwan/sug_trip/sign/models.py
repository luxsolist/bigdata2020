from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=200)
    user_pw = models.CharField(max_length=200)
    user_sex = models.CharField(max_length=200)
    user_age = models.CharField(max_length=200)
    user_add = models.CharField(max_length=200)
    user_email = models.CharField(max_length=100)
    user_fav_spot1 = models.CharField(max_length=100)
    user_fav_spot2 = models.CharField(max_length=100)
    user_fav_spot3 = models.CharField(max_length=100)