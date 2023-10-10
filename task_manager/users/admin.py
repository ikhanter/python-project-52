from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list = ('id', 'username', 'first_name', 'last_name')
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = [('created_at', admin.DateFieldListFilter), ('username', admin.FieldListFilter),]