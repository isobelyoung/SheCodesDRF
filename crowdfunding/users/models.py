from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_picture = models.URLField(blank = True)
    business_name = models.CharField(max_length = 400, blank = True)
    

    def __str__(self):
        return self.username
