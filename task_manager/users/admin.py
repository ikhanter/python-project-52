from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name')
    search_fields = ('username', 'first_name', 'last_name')