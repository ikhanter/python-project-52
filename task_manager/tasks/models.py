from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    labels = models.ManyToManyField(Label, blank=True)
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='executor_tasks',
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='creator_tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)
