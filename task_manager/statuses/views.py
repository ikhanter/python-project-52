from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Status
from .forms import StatusesCreateForm


# Create your views here.
class StatusesIndexView(LoginRequiredMixin, ListView):

    model = Status
    template_name = 'statuses/statuses_index.html'
    context_object_name = 'statuses'


class StatusesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Status
    form_class = StatusesCreateForm
    template_name = 'statuses/statuses_create.html'
    success_message = gettext_lazy('Status was created successfully')
    success_url = reverse_lazy('statuses_index')


class StatusesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Status
    form_class = StatusesCreateForm
    template_name = 'statuses/statuses_update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = gettext_lazy('Status was updated successfully')
    context_object_name = 'status'


class StatusesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'statuses/statuses_delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = gettext_lazy('Status was deleted')
    context_object_name = 'status'

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.add_message(
                request,
                messages.ERROR,
                gettext_lazy('You can\'t delete status until it\'s \
                             connected with active tasks'),
            )
        return redirect('statuses_index')
