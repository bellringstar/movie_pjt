from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    self_introduction = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    pass