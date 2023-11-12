from django import forms
from .models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from django.utils.translation import gettext_lazy


class TasksCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
            'executor': gettext_lazy('Executor'),
            'labels': gettext_lazy('Labels'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].label_from_instance = lambda obj: obj.name
        self.fields['status'].queryset = Status.objects.order_by('name')
        self.fields['executor'].label_from_instance = \
            lambda obj: obj.get_full_name()
        self.fields['executor'].queryset = \
            CustomUser.objects.order_by('first_name', 'last_name')
        self.fields['labels'].label_from_instance = lambda obj: obj.name
        self.fields['labels'].queryset = Label.objects.order_by('name')
