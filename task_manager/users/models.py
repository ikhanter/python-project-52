from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(auto_created=True)
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.full_name = self.get_full_name()
