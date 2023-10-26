from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)