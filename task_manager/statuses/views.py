from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy
from django.views import View
from .models import Status
from .forms import StatusesCreateForm

# Create your views here.
class StatusesIndexView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/statuses_index.html', {
            'statuses': statuses,
        })
    

class StatusesCreateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = StatusesCreateForm(label_suffix='')
        return render(request, 'statuses/statuses_create.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = StatusesCreateForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('Status was created successfully.'))
            return redirect('statuses_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('Status with this name already exists.'))
        return render(request, 'statuses/statuses_create.html', {
            'form': form,
        })


class StatusesUpdateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusesCreateForm(instance=status, label_suffix='')
        return render(request, 'statuses/statuses_update.html', {
            'form': form,
            'pk': status.pk,
        })
    
    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusesCreateForm(request.POST, instance=status)
        form.save()
        messages.add_message(request, messages.SUCCESS, gettext_lazy('Status was updated successfully.'))
        return redirect('statuses_index')


class StatusesDeleteView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        # TODO: add check if status is linked with task. You can't delete this if task exists.
        return render(request, 'statuses/statuses_delete.html', {
            'pk': status.pk,
        })
    
    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        status.delete()
        messages.add_message(request, messages.SUCCESS, gettext_lazy('Status was deleted.'))
        return redirect('statuses_index')
