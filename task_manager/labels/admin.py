from django.contrib import admin
from .models import Label


# Register your models here.
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']  # noqa: E501
    list_filter = ['name']
    search_fields = ['name']
