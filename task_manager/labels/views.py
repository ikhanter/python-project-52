from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from task_manager.tasks.models import Task
from .models import Label
from .forms import LabelsCreateForm


# Create your views here.
class LabelsIndexView(LoginRequiredMixin, ListView):

    model = Label
    template_name = 'labels/labels_index.html'
    context_object_name = 'labels'


class LabelsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Label
    template_name = 'labels/labels_create.html'
    form_class = LabelsCreateForm
    success_url = reverse_lazy('labels_index')
    success_message = gettext_lazy('Label was created successfully')


class LabelsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Label
    form_class = LabelsCreateForm
    template_name = 'labels/labels_update.html'
    success_url = reverse_lazy('labels_index')
    success_message = gettext_lazy('Label was updated successfully')
    context_object_name = 'label'


class LabelsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Label
    template_name = 'labels/labels_delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = gettext_lazy('Label was deleted successfully')
    context_object_name = 'label'

    def has_linked_tasks(self, label):
        try:
            if Task.objects.filter(labels=label).exists():
                raise IntegrityError
        except IntegrityError:
            return True
        return False

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, pk=kwargs['pk'])
        if not self.has_linked_tasks(label):
            super().post(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('Label is linked with tasks. \
                         Delete linked tasks firstly'),
        )
        return redirect('labels_index')
