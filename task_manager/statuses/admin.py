from django.contrib import admin
from .models import Status


# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'created_at',)
    list_filter = ('status_name',)
    search_fields = ('status_name',)
