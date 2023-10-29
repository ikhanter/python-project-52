from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy
from .models import Task
from .forms import TasksCreateForm

# Create your views here.
class TasksIndexView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/tasks_index.html', {
            'tasks': tasks,
        })
    
    # TODO: make a filter


class TasksCreateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = TasksCreateForm(label_suffix='')
        return render(request, 'tasks/tasks_create.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = TasksCreateForm(request.POST, label_suffix='')
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Task was created successfully.'))
            return redirect('tasks_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('Task was not created. Please, fill the fields correctly.'))
        return render(request, 'tasks/tasks_create.html', {
            'form': form,
        })


class TasksShowView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'tasks/tasks_show.html', {
            'task': task,
        })
    

class TasksUpdateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.creator == request.user:
            form = TasksCreateForm(instance=task, label_suffix='')
            return render(request, 'tasks/tasks_update.html', {
                'form': form,
                'pk': kwargs['pk'],
            })
        messages.add_message(request, messages.ERROR, gettext_lazy('You don\'t have permissions to update foreign tasks.'))
        return redirect('tasks_index')
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.creator == request.user:
            form = TasksCreateForm(request.POST, instance=task, label_suffix='')
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, gettext_lazy('Task was updated successfully.'))
                return redirect('tasks_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('You don\'t have permissions to update foreign tasks.'))
        return redirect('tasks_index')


class TasksDeleteView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.creator == request.user:
            return render(request, 'tasks/tasks_delete.html', {
                'pk': kwargs['pk'],
            })
        messages.add_message(request, messages.ERROR, gettext_lazy('You don\'t have permissions to delete foreign tasks.'))
        return redirect('tasks_index')
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if task.creator == request.user:
            task.delete()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Task was deleted successfully.'))
            return redirect('tasks_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('You don\'t have permissions to delete foreign tasks.'))
        return redirect('tasks_index')