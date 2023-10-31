from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy
from task_manager.tasks.models import Task
from .models import Label
from .forms import LabelsCreateForm


# Create your views here.
class LabelsIndexView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/labels_index.html', {
            'labels': labels,
        })


class LabelsCreateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = LabelsCreateForm()
        return render(request, 'labels/labels_create.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = LabelsCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Label was created successfully.'))  # noqa: 501
            return redirect('labels_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('This label already exists.'))  # noqa: 501
        return render(request, 'labels/labels_create.html', {
            'form': form,
        })


class LabelsUpdateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        label = get_object_or_404(Label, pk=kwargs['pk'])
        form = LabelsCreateForm(instance=label)
        return render(request, 'labels/labels_update.html', {
            'form': form,
            'pk': label.pk,
        })

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, pk=kwargs['pk'])
        form = LabelsCreateForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Label was updated successfully.'))  # noqa: 501
            return redirect('labels_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('This label already exists.'))  # noqa: 501
        return render(request, 'labels/labels_update.html', {
            'form': form,
        })


class LabelsDeleteView(LoginRequiredMixin, View):

    login_url = '/login/'

    def has_linked_tasks(self, label):
        try:
            if Task.objects.filter(labels=label).exists():
                raise IntegrityError
        except IntegrityError:
            return True
        return False

    def get(self, request, *args, **kwargs):
        label = get_object_or_404(Label, pk=kwargs['pk'])
        if not self.has_linked_tasks(label):
            return render(request, 'labels/labels_delete.html', {
                'pk': label.pk,
            })
        messages.add_message(request, messages.ERROR, gettext_lazy('Label is linked with tasks. Delete linked tasks firstly.'))  # noqa: 501
        return redirect('labels_index')

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, pk=kwargs['pk'])
        if not self.has_linked_tasks(label):
            label.delete()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Label was deleted successfully.'))  # noqa: 501
            return redirect('labels_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('Label is linked with tasks. Delete linked tasks firstly.'))  # noqa: 501
        return redirect('labels_index')
