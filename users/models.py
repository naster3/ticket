from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer= models.BooleanField(default=False)
    is_enginner= models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.username