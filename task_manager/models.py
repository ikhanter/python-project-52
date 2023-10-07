from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimestampedModel):
    first_name = models.CharField()
    last_name = models.CharField()
    username = models.CharField(validators=[MaxLengthValidator(150)], blank=False)
    password = models.CharField(validators=[MinLengthValidator(3)], blank=False)

    def __str__(self):
        return self.name