from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from .filters import TaskFilter
from .models import Task
from .forms import TasksCreateForm
from task_manager.mixins import CheckUserForTasksMixin


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
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = self.request.user
            task.save()
            form.save_m2m()
        return super().form_valid(form)


class TasksShowView(LoginRequiredMixin, DetailView):

    model = Task
    template_name = 'tasks/tasks_show.html'
    context_object_name = 'task'


class TasksUpdateView(
    CheckUserForTasksMixin,
    SuccessMessageMixin,
    UpdateView,
):

    model = Task
    login_url = '/login/'
    template_name = 'tasks/tasks_update.html'
    context_object_name = 'task'
    form_class = TasksCreateForm
    success_message = gettext_lazy('Task was updated successfully')
    success_url = reverse_lazy('tasks_index')

    def get(self, request, *args, **kwargs):
        if self.is_user_is_author:
            return super().get(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You don\'t have permissions \
                         to update foreign tasks.'),
        )
        return redirect('tasks_index')

    def post(self, request, *args, **kwargs):
        if self.is_user_is_author:
            return super().post(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You don\'t have permissions \
                         to update foreign tasks.'),
        )
        return redirect('tasks_index')


class TasksDeleteView(
    CheckUserForTasksMixin,
    SuccessMessageMixin,
    DeleteView,
):

    model = Task
    login_url = '/login/'
    template_name = 'tasks/tasks_delete.html'
    context_object_name = 'task'
    success_message = gettext_lazy('Task was deleted successfully')
    success_url = reverse_lazy('tasks_index')

    def get(self, request, *args, **kwargs):
        if self.is_user_is_author:
            return super().get(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You don\'t have permissions \
                         to delete foreign tasks.'),
        )
        return redirect('tasks_index')

    def post(self, request, *args, **kwargs):
        if self.is_user_is_author:
            return super().post(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You don\'t have permissions \
                         to delete foreign tasks.'),
        )
        return redirect('tasks_index')
