from django.contrib import admin
from task_manager.tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'status', 'executor', 'creator')  # noqa: E501
    list_filter = ('name', 'status', 'executor', 'creator')
    search_fields = ('name', 'status', 'executor', 'creator')
