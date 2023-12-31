from django import forms
from django.http.response import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from .filters import TaskFilter
from .mixins import CheckUserForTasksMixin
from .models import Task
from .forms import TasksCreateForm
from task_manager.mixins import CheckUserMixin


# Create your views here.
class TasksIndexView(LoginRequiredMixin, FilterView):

    model = Task
    template_name = 'tasks/tasks_index.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class TasksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Task
    template_name = 'tasks/tasks_create.html'
    form_class = TasksCreateForm
    success_url = reverse_lazy('tasks_index')
    success_message = gettext_lazy('Task was created successfully')

    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TasksShowView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = 'tasks/tasks_show.html'
    context_object_name = 'task'


class TasksUpdateView(
    LoginRequiredMixin,
    CheckUserMixin,
    SuccessMessageMixin,
    CheckUserForTasksMixin,
    UpdateView,
):

    model = Task
    login_url = '/login/'
    template_name = 'tasks/tasks_update.html'
    context_object_name = 'task'
    form_class = TasksCreateForm
    success_message = gettext_lazy('Task was updated successfully')
    success_url = reverse_lazy('tasks_index')
    error_message = gettext_lazy('You don\'t have permissions \
                                 to update foreign tasks.')
    no_permission_redirect_url = reverse_lazy('tasks_index')


class TasksDeleteView(
    LoginRequiredMixin,
    CheckUserMixin,
    SuccessMessageMixin,
    CheckUserForTasksMixin,
    DeleteView,
):

    model = Task
    login_url = '/login/'
    template_name = 'tasks/tasks_delete.html'
    context_object_name = 'task'
    success_message = gettext_lazy('Task was deleted successfully')
    success_url = reverse_lazy('tasks_index')
    error_message = gettext_lazy('You don\'t have permissions \
                                 to delete foreign tasks.')
    no_permission_redirect_url = reverse_lazy('tasks_index')
