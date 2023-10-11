from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
