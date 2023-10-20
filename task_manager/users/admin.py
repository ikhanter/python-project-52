from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = ('id', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser')
    list_filter = ('username', 'first_name')
    search_fields = ('username', 'first_name', 'last_name')
