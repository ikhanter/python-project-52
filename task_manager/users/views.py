from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.translation import gettext_lazy
from .forms import UsersCreateForm
from .models import CustomUser
from django.db.models import ProtectedError


# Create your views here.
class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UsersCreateForm(label_suffix='')
        return render(request, 'users/users_create.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = UsersCreateForm(request.POST, label_suffix='')
        try:
            form.clean_password()
        except ValidationError:
            pass
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('User was created successfully.'))  # noqa: E501
            return redirect('login')
        messages.add_message(request, messages.ERROR, gettext_lazy('User is not created. Please, check the fields.'))  # noqa: E501
        return render(request, 'users/users_create.html', {
            'form': form,
        })


class UsersIndexView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/users_index.html', {
            'users': users
        })


class UsersUpdateView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=kwargs['pk'])
        if request.user.pk == user.pk:
            form = UsersCreateForm(instance=user, label_suffix='')
            return render(request, 'users/users_update.html', {
                'form': form,
            })
        messages.add_message(request, messages.ERROR, gettext_lazy('You do not have permissions to change this user.'))  # noqa: E501
        return redirect('users_index')

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if request.user.pk == user.pk:
            form = UsersCreateForm(request.POST, instance=user)
            try:
                form.clean_password()
            except ValidationError:
                pass
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, gettext_lazy('User was updated successfully.'))  # noqa: E501
                return redirect('users_index')
        messages.add_message(request, messages.ERROR, gettext_lazy('User is not updated. Please, check the fields.'))  # noqa: E501
        return render(request, 'users/users_update.html', {
            'form': form,
        })


class UsersDeleteView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=kwargs['pk'])
        if request.user.pk == user.pk:
            return render(request, 'users/users_delete.html', {'id': kwargs['pk']})  # noqa: E501
        messages.add_message(request, messages.ERROR, gettext_lazy('You do not have permissions to delete this user.'))  # noqa: E501
        return redirect('users_index')

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = get_object_or_404(CustomUser, pk=user_id)
        if request.user.pk == user.pk:
            try:
                user.delete()
            except ProtectedError:
                messages.add_message(request, messages.ERROR, gettext_lazy('You can\t delete yourself until you have active tasks.'))  # noqa: E501
                return redirect('users_index')
            messages.add_message(request, messages.SUCCESS, gettext_lazy('User was deleted.'))  # noqa: E501
        return redirect('users_index')
