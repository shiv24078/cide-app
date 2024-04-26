from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    signup_date = models.DateTimeField(auto_now_add=True)
