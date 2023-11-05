from django.contrib import admin
from .models import Status


# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    list_filter = ('name',)
    search_fields = ('name',)
