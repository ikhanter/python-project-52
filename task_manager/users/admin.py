from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = ('id', 'username', 'full_name', 'is_active', 'is_superuser')  # noqa: E501
    list_filter = ('username', 'full_name')
    search_fields = ('username', 'first_name', 'last_name')
