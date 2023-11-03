from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.get_full_name()} ({self.username})'.strip()