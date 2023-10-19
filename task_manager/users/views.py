from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.translation import gettext_lazy
from .forms import UsersCreateForm
from .models import CustomUser

# Create your views here.
class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UsersCreateForm(label_suffix='')
        return render(request, 'users/users_create.html', {
            'form': form,
        })
    
    def post(self, request, *args, **kwargs):
        form = UsersCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('User was created successfully.'))
            return redirect('login')
        messages.add_message(request, messages.ERROR, gettext_lazy('User is not created. Please, check the fields.'))
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

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=kwargs['pk'])
        form = UsersCreateForm(instance=user, label_suffix='')
        return render(request, 'users/users_update.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=kwargs['pk'])
        form = UsersCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, gettext_lazy('User was updated successfully.'))
            return redirect('login')
        messages.add_message(request, messages.ERROR, gettext_lazy('User is not updated. Please, check the fields.'))
        return render(request, 'users/users_create.html', {
            'form': form,
        })


class UsersDeleteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/users_delete.html', {'id': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.get(id=user_id)
        if user:
            user.delete()
            messages.add_message(request, messages.SUCCESS, 'User was deleted.')
        return redirect('index')
