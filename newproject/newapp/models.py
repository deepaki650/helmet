from django.db import models

# Create your models here.


class register(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
