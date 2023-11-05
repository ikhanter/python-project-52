import django_filters
from django.utils.translation import gettext_lazy
from .models import Task
from django import forms
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=gettext_lazy('Status'),
        label_suffix='',
        queryset=Status.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    executor = django_filters.ModelChoiceFilter(
        label=gettext_lazy('Executor'),
        label_suffix='',
        queryset=CustomUser.objects.order_by('first_name', 'last_name'),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    labels = django_filters.ModelMultipleChoiceFilter(
        label=gettext_lazy('Labels'),
        label_suffix='',
        queryset=Label.objects.order_by('name'),
    )
    self_tasks = django_filters.BooleanFilter(
        label=gettext_lazy('Only my tasks'),
        label_suffix='',
        method='filter_by_user',
        widget=forms.Select(
            choices=[(True, gettext_lazy('Yes')), (False, gettext_lazy('No'))],
            attrs={'class': 'form-control'},
        ),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def filter_by_user(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(creator_id=self.user.pk)
