from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from .forms import UsersCreateForm
from .models import CustomUser
from django.db.models import ProtectedError
from task_manager.mixins import CheckUserForContentMixin


# Create your views here.
class UsersCreateView(SuccessMessageMixin, CreateView):

    model = get_user_model()
    form_class = UsersCreateForm
    template_name = 'users/users_create.html'
    success_message = gettext_lazy('User was created successfully.')
    success_url = reverse_lazy('login')


class UsersIndexView(ListView):

    model = get_user_model()
    template_name = 'users/users_index.html'
    context_object_name = 'users'


class UsersUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
    CheckUserForContentMixin,
):

    model = get_user_model()
    form_class = UsersCreateForm
    template_name = 'users/users_update.html'
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User was updated successfully')

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=kwargs['pk'])
        if self.is_user_is_author(request.user, user):
            return super().get(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You do not have permissions to change this user'),
        )
        return redirect('users_index')

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if self.is_user_is_author(request.user, user):
            return super().post(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You do not have permissions to change this user'),
        )
        return redirect('users_index')


class UsersDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
    CheckUserForContentMixin,
):

    model = get_user_model()
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('users_index')
    success_message = gettext_lazy('User was deleted')

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if self.is_user_is_author(request.user, user):
            return super().get(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You do not have permissions to delete this user'),
        )
        return redirect('users_index')

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if self.is_user_is_author(request.user, user):
            try:
                super().post(request, *args, *kwargs)
            except ProtectedError:
                messages.add_message(
                    request,
                    messages.ERROR,
                    gettext_lazy('You can\t delete yourself \
                                 until you have active tasks'),
                )
                return redirect('users_index')
            return redirect('users_index')
        messages.add_message(
            request,
            messages.ERROR,
            gettext_lazy('You do not have permissions to delete this user'),
        )
        return redirect('users_index')
