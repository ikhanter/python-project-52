from django import forms
from django.db.models.functions import Concat
from django.db.models import Value
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy


class TasksCreateForm(forms.ModelForm):
  
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']
        labels = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
            'executor': gettext_lazy('Executor'),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].label_from_instance = lambda obj: obj.status_name
        self.fields['status'].queryset = Status.objects.order_by('status_name')
        self.fields['executor'].label_from_instance = lambda obj: obj.full_name
        self.fields['executor'].queryset = CustomUser.objects.order_by('first_name', 'last_name')
