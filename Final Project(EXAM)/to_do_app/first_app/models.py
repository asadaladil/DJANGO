from django.db import models
    

class UserAccount(models.Model):
    user_name=models.CharField(max_length=20,unique=True,blank=False)
    first_name=models.CharField(max_length=20,blank=False)
    last_name=models.CharField(max_length=20,blank=False)
    University=models.CharField(max_length=70,blank=False)
    