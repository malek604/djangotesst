from django.db import models




class CustomUser(models.Model):
    email = models.EmailField(unique=True) 
    username=models.CharField( max_length = 150)
    id = models.BigAutoField(primary_key=True)
    password=models.CharField(max_length = 150)


# class user_login(models.Model):
