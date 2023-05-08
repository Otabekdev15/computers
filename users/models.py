from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    person_image = models.ImageField(default='default_profile_pic.jpg')
